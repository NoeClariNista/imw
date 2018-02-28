<!DOCTYPE html>
<html>
<head>
    <title>Ejercicio 4.</title>
</head>
<body>
<form action="ejercicio4.php" method="post">
    <table>
        <tr>
            <td> Filas. </td>
            <td> <input type="text" name="rows" /> </td>
        </tr>
        <tr>
            <td> Columnas. </td>
            <td> <input type="text" name="columns" /> </td>
        </tr>
        <tr>
            <td> <input type="submit" value="Enviar" /> </td>
        </tr>
    </table>
</form>
<table border="1">
    <?php
        if (isset($_POST["rows"]) and isset($_POST["columns"])) {
            $rows = (int)$_POST["rows"];
            $columns = (int)$_POST["columns"];
            $number_rows = 1;
            $number_columns = 1;
            if ($rows >= 1 and $columns >= 1) {
                echo ("<p>$rows Filas Y $columns Columnas.</p>");
                while ($number_rows <= $rows) {
                    $number_rows++;
                    echo("<tr>");
                    while ($number_columns <= $columns) {
                        $number_columns++;
                        echo ("<td> Texto. </td>");                
                    }
                    $number_columns = 1;
                    echo ("</tr>");
                }
            }
            else {
                echo ("<p> ¡Error! Los Dos Números Tienen Que Ser Mayores Que 0. </p>");
            }
        }
    ?>
</body>
</html>
