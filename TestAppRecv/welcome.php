<html>
<body>

Welcome <?php echo $_POST["name"]; ?><br>
Your email address is: <?php echo $_POST["email"]; ?><br>
Opening file<br>
<?$fid = fopen("subsDatabase.csv", "a"); ?>
<!-- File open <?php echo $fid; ?><br> -->
<?$rval = bool fclose($fid); ?>
<!-- File closed result <?php echo $rval; ?> -->
</body>
</html>
