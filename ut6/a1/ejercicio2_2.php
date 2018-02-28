<?php
    $name = $_POST['name'];
    $surnames = $_POST['surnames'];
    $salary = $_POST['salary'];
    $age = $_POST['age'];
    $salary = (float)$salary;
    $age = (int)$age;
    if (($salary >= 1000) and ($salary <= 2000)) {
        if ($age <= 45) {
       	    $final_salary = $salary * 1.10;
        }
        else {
            $final_salary = $salary * 1.03;
        }
        echo ("$name $surnames con $age años cobrará $final_salary €.");
    } 
    elseif ($salary < 1000) {
        if ($age < 30 ) {
            $final_salary = 1100;
        } 
        elseif ($age >= 30 and $age <= 45) {
            $final_salary = $salary * 1.03;
        } 
        else {
            $final_salary = $salary * 1.15;
        }
        echo ("$name $surnames con $age años cobrará $final_salary €.");
    } 
    else {
        echo ("$name $surnames con $age años cobrará $salary €.");
    }
?>
