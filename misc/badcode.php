<?php
	$productDescription = $_GET['description'];
    $product_name = $_GET["product_name"];
    $id = $_GET['id'];
	
    $db = new mysqli("example.com", "user", "password", "database");
    $UpdateQuery =
                "UPDATE product 
                SET description = '{$productDescription}' ,name = '{$product_name}'
                WHERE prodcut_id = '{$id}';";
    $mysqli->query($UpdateQuery)
?>