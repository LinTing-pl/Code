
public class Dog1 {
    protected String name;
    private int id;

    public Dog1(String myName, int myid) {
        name = myName;
        id = myid;
    }
    public Dog1(){
        System.out.println("111");
    }
    public void eat() {
        System.out.println(name + "正在吃");
    }

    public void sleep() {
        System.out.println(name + "正在睡");
    }

    public void introduction() {
        System.out.println("大家好！我是" + id + "号" + name + ".");
    }
    enum Color{
        Red,Blue,Yellow;
        private Color(){
            System.out.println("call"+this);
        }
    }
    public static void main(String[] args) {
        System.out.println("Hellow World");
        B b = new B("小狗",12);
        b.eat();
        b.sleep();
        b.introduction();
        b.bark();
        Color c=Color.Yellow;
        System.out.println(c);
        for(Color d:Color.values()){
            System.out.println(d);

        }
    }
}


class B extends Dog1 {
    public B(String myName, int myid) {
        super(myName, myid);
    }

    @Override
    public void eat() {
        System.out.println(name+"吃饱了");
    }
    void bark(){
        System.out.println("wowowo");
    }
}

