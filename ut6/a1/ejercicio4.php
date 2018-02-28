<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Ejercicio 4.</title>
    </head>
    <body>
        <form action="index.php" method="post">
            <label for="rows">Filas.</label>
                <input type="text" name="rows"/><br>
            <label for="columns">Columnas.</label>
                <input type="text" name="columns"/><br>
            <input type="submit" value="Enviar"/>
        </form>
        <table border="1">
        <?php
            if (isset($_POST["rows"]) and isset($_POST["columns"])) {
                $rows = (float)$_POST["rows"];
                $columns = (float)$_POST["columns"];
                $number_rows = 1;
                $number_columns = 1;
                if ($rows >= 1 and $columns >= 1) {
                    echo("<p>Filas Y Columnas.</p>");
                    while ($number_rows<=$rows) {
                        $number_rows++;
                        echo("<tr>");
                        while ($number_columns <= $columnas) {
                            $number_columns++;
                            echo("<td>Prueba.</td>");
                        }
                        $number_columns = 1;
                        echo("</tr>");
                    }
                }
                else {
                    echo("Valor Erroneo.");
                }
            }
        ?>
        </table>
    </body>
</html>
