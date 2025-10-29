<?php
include ("calculations.php");

$result = new Calculating();

$n = 10;
echo "Fibonacci number: ";
$result->fibonacci($n);

echo "<div> Arithmetic progression: ";
$result->progression();

$number = 5;
$calculator = new FactorialCalculator($number);
$result = $calculator->calculateFactorial();

echo "<div>Factorial of $number: $result";
?>