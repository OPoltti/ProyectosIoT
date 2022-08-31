<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Bomba de jeringa</title>
	<link rel="icon" href="logo1.ico">
	<link rel="stylesheet" type="text/css" href="estilo.css">
	<link rel="stylesheet" type="text/css" href="normalize.css">
	<link href="https://fonts.googleapis.com/css2?family=Kanit:wght@100&display=swap" rel="stylesheet">
</head>
<body>
	<h1>CONTROL Y MONITOREO DE UNA BOMBA DE JERINGA</h1>
	<header>
			<nav>
				<ul>
					<li> <a href="index.html">Inicio</a></li>
					<li> <a href="fundamento.html">Fundamento</a></li>
					<li> <a href="formulacion.html">Entrada de datos</a></li>
				</ul>
			</nav>
	</header>
	<h1></h1>
	<p>Proyecto de Instrumentación Electrónica</p>
	<img src="logo2.jpg" align="right">
	<hr>
	<h1></h1>
	<h2 class="datos">
		<label>Posicionamiento/Calibracion</label>
        <select id="Estadobox1">
            <option value="1">ON</option>
            <option value="0">OFF</option>
        </select>
        <button id="Insertarbtn1">Ejecutar</button>
	</h2>
	<h2 class="datos">
		<label>Velocidad de flujo (ml/s)</label>
        <select id="Estadobox2">
            <option value="1">v1 = 1.67 ml/s</option>
            <option value="2">v2 = 0.32 ml/s</option>
            <option value="3">v3 = 0.18 ml/s</option>
        </select>
        <button id="Insertarbtn2">Ejecutar</button>
	</h2>
	<h2 class="datos">
		<label for>Volumen a suministrar (ml):</label>
        <select id="Estadobox3">
            <option value="1">1 ml</option>
            <option value="2">2 ml</option>
            <option value="3">3 ml</option>
            <option value="4">4 ml</option>
            <option value="5">5 ml</option>
            <option value="0">OFF(CALIBRANDO)</option>
        </select>
        <button id="Insertarbtn3">Ejecutar</button>
	</h2>

<!--------------------------------IMPORTS + CONFIGURATION--------------------------------------->
		<script type="module">
			// Import the functions you need from the SDKs you need
			import { initializeApp } from "https://www.gstatic.com/firebasejs/9.4.1/firebase-app.js"
			// TODO: Add SDKs for Firebase products that you want to use
			// https://firebase.google.com/docs/web/setup#available-libraries
			
			// Your web app's Firebase configuration
			// For Firebase JS SDK v7.20.0 and later, measurementId is optional
			const firebaseConfig = {
			apiKey: "AIzaSyDbWGV6W8fMAdO0wXWEkSrbSI2MNLFApA0",
			authDomain: "iot-bombadejeringa.firebaseapp.com",
			databaseURL: "https://iot-bombadejeringa-default-rtdb.firebaseio.com",
			projectId: "iot-bombadejeringa",
			storageBucket: "iot-bombadejeringa.appspot.com",
			messagingSenderId: "1045639348537",
			appId: "1:1045639348537:web:8a1cceeff0a73e082468e8",
			measurementId: "G-6T2SXZ0S78"
			};
			// Initialize Firebase
            const app = initializeApp(firebaseConfig);

            import{getDatabase, ref, get, set, child, update, remove}
            from "https://www.gstatic.com/firebasejs/9.4.1/firebase-database.js";

            const db = getDatabase();
			const db2 = getDatabase();
            const db3 = getDatabase();
			const db4 = getDatabase();


            //-----Referencias---//
            var estadobox1 = document.getElementById("Estadobox1");
            var insertarbtn1 = document.getElementById("Insertarbtn1");
			var estadobox2 = document.getElementById("Estadobox2");
            var insertarbtn2 = document.getElementById("Insertarbtn2");
            var estadobox3 = document.getElementById("Estadobox3");
            var insertarbtn3 = document.getElementById("Insertarbtn3");
			//var estadobox4 = document.getElementById("Estadobox4");
            //var insertarbtn4 = document.getElementById("Insertarbtn4");

             //---- Insertamos la funcion data ----//
            function InsertData() {
                set(ref(db,'/CALIBRACION/'), {
                    Posicion: parseInt(estadobox1.value)
                })
                .then(() => {
                     alert("DATOS ENVIADOS EXITOSAMENTE");
                 })
                .catch((error) => {
                    alert("Error inusual" + error);
                 });
             }
            //---Asignar eventos a botones ---///
            Insertarbtn1.addEventListener('click', InsertData);
			
			function InsertData2() {
                set(ref(db2,'/VELOCIDAD/'), {
                    VELOCIDAD: parseInt(estadobox2.value)
                })
                .then(() => {
                     alert("DATOS ENVIADOS EXITOSAMENTE");
                 })
                .catch((error) => {
                    alert("Error inusual" + error);
                 });
             }
            //---Asignar eventos a botones ---///
            Insertarbtn2.addEventListener('click', InsertData2);


            function InsertData3() {
                set(ref(db3,'/VOLUMEN/'), {
                    VOLUMEN: parseInt(estadobox3.value)
                })
                .then(() => {
                     alert("DATOS ENVIADOS EXITOSAMENTE");
                 })
                .catch((error) => {
                    alert("Error inusual" + error);
                 });
             }
            //---Asignar eventos a botones ---///
            Insertarbtn3.addEventListener('click', InsertData3);

		</script>
</body>
</html>