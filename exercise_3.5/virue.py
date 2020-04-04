#1、病毒对象
public class Virus {}

#2、床位【隔离对象】

public class Bed extends Point{
    public Bed(int x, int y) {
        super(x, y);
    }
    private boolean isEmpty=true;

    public boolean isEmpty() {
        return isEmpty;
    }
    public void setEmpty(boolean empty) {
        isEmpty = empty;
    }
}

#3、主要参数【初始状态】，假设没有隔离，潜伏期为一天

public class Constants {
    public static int ORIGINAL_COUNT=50;//初始感染数量
    public static float BROAD_RATE = 0.8f;//传播率
    public static float SHADOW_TIME = 1;//潜伏时间
    public static int HOSPITAL_RECEIVE_TIME=10;//医院收治响应时间
    public static int BED_COUNT=0;//医院床位
    public static float u=0.99f;//流动意向平均值
}

#4、医院对象，随机分布，产生床位
public class Hospital {
    private int x=800;
    private int y=110;

    private int width;
    private int height=606;
    public int getWidth() {
        return width;
    }
    public int getHeight() {
        return height;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    private static Hospital hospital = new Hospital();
    public static Hospital getInstance(){
        return hospital;
    }
    private Point point = new Point(800,100);
    private List<Bed> beds = new ArrayList<>();

    private Hospital() {
        if(Constants.BED_COUNT==0){
            width=0;
            height=0;
        }
        int column = Constants.BED_COUNT/100;
        width = column*6;
        for(int i=0;i<column;i++){
            for(int j=10;j<=610;j+=6){
                Bed bed = new Bed(point.getX()+i*6,point.getY()+j);
                beds.add(bed);
            }
        }
    }

    public Bed pickBed(){
        for(Bed bed:beds){
            if(bed.isEmpty()){
                return bed;
            }
        }
        return null;
    }
}


#5、流动目的地

public class MoveTarget {
    private int x;
    private int y;
    private boolean arrived=false;

    public MoveTarget(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public boolean isArrived() {
        return arrived;
    }

    public void setArrived(boolean arrived) {
        this.arrived = arrived;
    }
}

#6、人员【流动及感染】

public class Person {
    private City city;
    private int x;
    private int y;
    private MoveTarget moveTarget;
    int sig=1;
    double targetXU;
    double targetYU;
    double targetSig=50;
    public interface State{
        int NORMAL = 0;
        int SUSPECTED = NORMAL+1;
        int SHADOW = SUSPECTED+1;
        int CONFIRMED = SHADOW+1;
        int FREEZE = CONFIRMED+1;
        int CURED = FREEZE+1;
    }

    public Person(City city, int x, int y) {
        this.city = city;
        this.x = x;
        this.y = y;
        targetXU = 100*new Random().nextGaussian()+x;
        targetYU = 100*new Random().nextGaussian()+y;

    }
    public boolean wantMove(){
        double value = sig*new Random().nextGaussian()+Constants.u;
        return value>0;
    }

    private int state=State.NORMAL;

    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    int infectedTime=0;
    int confirmedTime=0;
    public boolean isInfected(){
        return state>=State.SHADOW;
    }
    public void beInfected(){
        state = State.SHADOW;
        infectedTime=MyPanel.worldTime;
    }

    public double distance(Person person){
        return Math.sqrt(Math.pow(x-person.getX(),2)+Math.pow(y-person.getY(),2));
    }

    private void freezy(){
        state = State.FREEZE;
    }
    private void moveTo(int x,int y){
        this.x+=x;
        this.y+=y;
    }
    private void action(){
        if(state==State.FREEZE){
            return;
        }
        if(!wantMove()){
            return;
        }
        if(moveTarget==null||moveTarget.isArrived()){

            double targetX = targetSig*new Random().nextGaussian()+targetXU;
            double targetY = targetSig*new Random().nextGaussian()+targetYU;
            moveTarget = new MoveTarget((int)targetX,(int)targetY);

        }


        int dX = moveTarget.getX()-x;
        int dY = moveTarget.getY()-y;
        double length=Math.sqrt(Math.pow(dX,2)+Math.pow(dY,2));

        if(length<1){
            moveTarget.setArrived(true);
            return;
        }
        int udX = (int) (dX/length);
        if(udX==0&&dX!=0){
            if(dX>0){
                udX=1;
            }else{
                udX=-1;
            }
        }
        int udY = (int) (dY/length);
        if(udY==0&&udY!=0){
            if(dY>0){
                udY=1;
            }else{
                udY=-1;
            }
        }

        if(x>700){
            moveTarget=null;
            if(udX>0){
                udX=-udX;
            }
        }
        moveTo(udX,udY);


    }

    private float SAFE_DIST = 2f;

    public void update(){
        if(state>=State.FREEZE){
            return;
        }
        if(state==State.CONFIRMED&&MyPanel.worldTime-confirmedTime>=Constants.HOSPITAL_RECEIVE_TIME){
            Bed bed = Hospital.getInstance().pickBed();
            if(bed==null){
                System.out.println("隔离区没有空床位");
            }else{
                state=State.FREEZE;
                x=bed.getX();
                y=bed.getY();
                bed.setEmpty(false);
            }
        }
        if(MyPanel.worldTime-infectedTime>Constants.SHADOW_TIME&&state==State.SHADOW){
            state=State.CONFIRMED;
            confirmedTime = MyPanel.worldTime;
        }

        action();

        List<Person> people = PersonPool.getInstance().personList;
        if(state>=State.SHADOW){
            return;
        }
       for(Person person:people){
           if(person.getState()== State.NORMAL){
               continue;
           }
           float random = new Random().nextFloat();
           if(random<Constants.BROAD_RATE&&distance(person)<SAFE_DIST){
               this.beInfected();
           }
       }
    }
}

#7、汇总人数

public class PersonPool {
    private static PersonPool personPool = new PersonPool();
    public static PersonPool getInstance(){
        return personPool;
    }

    List<Person> personList = new ArrayList<Person>();

    public List<Person> getPersonList() {
        return personList;
    }

    private PersonPool() {
        City city = new City(400,400);
        for (int i = 0; i < 5000; i++) {
            Random random = new Random();
            int x = (int) (100 * random.nextGaussian() + city.getCenterX());
            int y = (int) (100 * random.nextGaussian() + city.getCenterY());
            if(x>700){
                x=700;
            }
            Person person = new Person(city,x,y);
            personList.add(person);
        }
    }
}

#8、分布点

public class Point {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
}

#9、显示面板，设置色块【红色：感染   黄色：潜伏  绿色：安全】






public class MyPanel extends JPanel implements Runnable {
   private int pIndex=0;
    public MyPanel() {
        this.setBackground(new Color(0x444444));
    }

    @Override
    public void paint(Graphics arg0) {
        super.paint(arg0);
        //draw border
        arg0.setColor(new Color(0x00ff00));
        arg0.drawRect(Hospital.getInstance().getX(),Hospital.getInstance().getY(),
                Hospital.getInstance().getWidth(),Hospital.getInstance().getHeight());
        List<Person> people = PersonPool.getInstance().getPersonList();
        if(people==null){
            return;
        }
        people.get(pIndex).update();
        for(Person person:people){

            switch (person.getState()){
                case Person.State.NORMAL:{
                    arg0.setColor(new Color(0xdddddd));

                }break;
                case Person.State.SHADOW:{
                    arg0.setColor(new Color(0xffee00));

                }break;
                case Person.State.CONFIRMED:
                case Person.State.FREEZE:{
                    arg0.setColor(new Color(0xff0000));

                }break;
            }
            person.update();
            arg0.fillOval(person.getX(), person.getY(), 3, 3);

        }
        pIndex++;
        if(pIndex>=people.size()){
            pIndex=0;
        }
    }

    public static int worldTime=0;
    @Override
    public void run() {
        while (true) {

            this.repaint();

            try {
                Thread.sleep(100);
                worldTime++;
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

#10、主程序【运行】
public class Main {
    public static void main(String[] args) {
        MyPanel p = new MyPanel();
        Thread panelThread = new Thread(p);
        JFrame frame = new JFrame();
        frame.add(p);
        frame.setSize(1000, 800);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panelThread.start();

        List<Person> people = PersonPool.getInstance().getPersonList();
        for(int i=0;i<Constants.ORIGINAL_COUNT;i++){
            int index = new Random().nextInt(people.size()-1);
            Person person = people.get(index);

            while (person.isInfected()){
                index = new Random().nextInt(people.size()-1);
                person = people.get(index);
            }
            person.beInfected();
        }
    }
}