<?php
class Password
{
    public function generateRandomCharacter($min, $max) {
        return chr(rand($min, $max));
    }

    public function generateLowercaseLetter() {
        return $this->generateRandomCharacter(97, 122);
    }

    public function generateUppercaseLetter() {
        return $this->generateRandomCharacter(65, 90);
    }

    public function generateNumber() {
        return $this->generateRandomCharacter(48, 57);
    }

    public function generateSymbol() {
        return $this->generateRandomCharacter(33, 47);
    }

    public function generatePassword($length, $lowercaseCount, $uppercaseCount, $numberCount, $symbolCount) {
        $password = '';

        for ($i = 0; $i < $lowercaseCount; $i++) {
            $password .= $this->generateLowercaseLetter();
        }

        for ($i = 0; $i < $uppercaseCount; $i++) {
            $password .= $this->generateUppercaseLetter();
        }

        for ($i = 0; $i < $numberCount; $i++) {
            $password .= $this->generateNumber();
        }

        for ($i = 0; $i < $symbolCount; $i++) {
            $password .= $this->generateSymbol();
        }

        $password = str_shuffle($password);

        while (strlen($password) < $length) {
            $password .= $this->generateRandomCharacter(33, 126);
        }

        return $password;
    }
}
$length = (int)readline("Enter the length of the password: ");
$lowercaseCount = (int)readline("Enter the amount of lowecraces in the password: ");
$uppercaseCount = (int)readline("Enter the amount of uppercases in the password: ");
$numberCount = (int)readline("Enter the amount of mumbers in the password: ");
$symbolCount = (int)readline("Enter the amount of symbols in the password: ");

$count = $lowercaseCount + $uppercaseCount + $numberCount + $symbolCount;

if ($length<$count)
{
    echo"\nThe length of the desirable password is too short than the amount of the desirable symbols.\nPassword would suit the amount of given symbols - $count\n";
}
elseif ($length>$count)
{
    echo"\nThe length of the desirable password is too long than the amount of the desirable symbols.\nPassword would suit the amount of given length - $length\n";
}

$generator = new Password();
$password = $generator->generatePassword($length, $lowercaseCount, $uppercaseCount, $numberCount, $symbolCount);
echo "\n$password\n";

?>
