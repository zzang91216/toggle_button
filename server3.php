<?php
    $host = 'your host';
    $user = 'rootuser';
    $pw = 'your pw';
    $dbName = 'new';
// Create connection
    $con=mysqli_connect($host, $user, $pw, $dbName);

    // Check connection
    if (mysqli_connect_errno()){
        echo "Failed to connect to MySQL: " . mysqli_connect_error();
    }
    //$sql="CREATE TABLE userstate2(id INT, name VARCHAR(30),age INT, result INT)";
    //if (mysqli_query($con,$sql)){
    //    echo "good  ";
    //}
    //else{
    //    echo "not   good  ";
    //}
    $id = $_POST['id'];
    $name = $_POST['name'];
    $age = (int)$_POST['age'];
    $result = (int)$_POST['result'];
    $time = (int)$_POST['time'];
    $query="insert into userstate2(id, name, age, result, timess)
        values('$id','$name','$age','$result','$time')";
    //$query = "DELETE FROM usertable";
    mysqli_query($con, $query);
    mysqli_close($con);
?>