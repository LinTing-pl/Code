import java.io.IOException;
import java.util.Scanner;

/**
 * @Projection: Dog
 * @Class: isSuShu
 * @Author: Linting 15019763969
 * @Date: 17:44 2022/3/11
 * @Description: TODO
 */
class isSuShu {
    public static boolean ShuShu(int num) {
        if (num <= 1) return false;
        if (num == 2) return true;
        for (int i = 2; i < num / 2 + 1; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num;
        boolean res = ShuShu(1133);
        do {
            System.out.println("输入一个整数，判断其是否是素数，输入数字0退出程序");
            num = input.nextInt();
            if (res) {
                System.out.println(1133 + "是素数");
            } else {
                System.out.println(1133 + "不是素数");
            }
        } while (num != 0);
    }
}

