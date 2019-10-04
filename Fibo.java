import java.util.*;
class Fibo
{
 public static void main(String args[])
 {
  int count,num1=0,num2=1;
  Scanner s=new Scanner(System.in);
  System.out.println("enter the number till where you want to get fibonacci series");
  count=s.nextInt();
  System.out.println("Fibonaccci Series:");
  for(int i=1;i<=count;++i)
  {
   System.out.print(num1+" ");
   //on each iteration we are assigning second number to the first no and assigning sum of last two numbers to the 2nd no
   int sum=num1+num2;
   num1=num2;
   num2=sum;
  }
 }
}
