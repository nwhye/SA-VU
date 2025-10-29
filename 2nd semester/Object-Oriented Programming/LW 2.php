<?php

class Calculating
{
  public function fibonacci($n)
  {

    $num1 = 0;
    $num2 = 1;

    $counter = 0;
    while ($counter < $n)
    {
        echo ', '.$num1;
        $num3 = $num2 + $num1;
        $num1 = $num2;
        $num2 = $num3;
        $counter = $counter + 1;
    }
  }
   public function progression()
   {
       $a = 1;
       $b = 100;
       $d = 15;

       $arr = range($a,$b,$d);
       echo implode(", ",$arr);
   }
}
$n = 10;
$result = new Calculating();
echo "Fibonacci number: ";
$result->fibonacci($n);
echo "<div> Arithmetic progression: ";
$result->progression();


?>
