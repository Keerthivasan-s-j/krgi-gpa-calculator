grades=['O','A+','A','B+','B','C','U']
semester = ["Select Semester","Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8"]

departments = [
    "Select Department",
    "Computer Science and Engineering",
    "Electrical and Electronics Engineering",
    "Electronics and Communication Engineering",
    "Mechanical Engineering",
    "Artificial Intelligence and Data Science",
    "Computer Science and Engineering (Artificial Intelligence and Machine Learning)",
    "Information Technology",
    "Computer Science and Business Systems"
]

cse = {
    "Semester 1": {
        "UHS1151 Technical English - I": 3,
        "UMA1151 Mathematics - I": 4,
        "UPH1151 Engineering Physics - I": 3,
        "UCY1151 Engineering Chemistry": 3,
        "UGE1151 Python Programming and Problem Solving": 3,
        "UBE1161 Basic Civil and Mechanical Engineering (Theory + Lab)": 4,
        "UBS1161 Physics and Chemistry Laboratory": 2,
        "UGE1161 Python Programming and Problem Solving Laboratory": 2
    },
    "Semester 2": {
        "UHS1251 Technical English - II": 3,
        "UMA1251 Mathematics - II": 4,
        "UPH1251 Engineering Physics - II": 3,
        "UGE1251 Environmental Science and Engineering": 3,
        "UGE1252 C Programming": 3,
        "UGE1253 Engineering Graphics": 3,
        "UBE1261 Basic Electrical and Electronics Engineering (Theory + Lab)": 3,
        "UGE1261 C Programming Laboratory": 2,
        "UHS1252 Professional skills - I": 1
    },
    "Semester 3": {
        "UMA1351 Discrete Mathematics and Graph Theory": 4,
        "UEC1351 Analog Electronic Circuits": 3,
        "UCS1301 Data Structures and Algorithm Analysis": 3,
        "UCS1302 Computer Organization and Architecture": 3,
        "UCS1303 Object Oriented Programming with Java": 3,
        "UCS1311 Data Structures and Algorithms Laboratory": 2,
        "UCS1312 Object Oriented Programming Laboratory": 2,
        "UEC1361 Analog Electronic Circuits Laboratory": 2,
        "UHS1361 Interpersonal Skills Laboratory": 1,
        "UHS1351 Professional Skills - II": 1
    },
    "Semester 4": {
        "UMA1454 Applied Probability Statistics and Numerical Analysis": 4,
        "UCS1401 Database Management Systems": 3,
        "UCS1402 Operating Systems": 3,
        "UCS1403 Software Engineering": 3,
        "UMG1052 Total Quality Management": 3,
        "UCS1411 Operating Systems Laboratory": 2,
        "UCS1412 Database Management Systems Laboratory": 2,
        "UCS1413 Mini Project": 2,
        "UHS1451 Professional Skills-III": 1
    },
    "Semester 5": {
        "UCS1501 Theory of Automata": 3,
        "UCS1502 Computer Networks": 3,
        "UCS1503 Artificial Intelligence": 3,
        "UCS1504 Mobile Computing": 3,
        "UCS1505 Internet of Things": 3,
        "Professional Elective-I": 3,
        "UCS1511 Mobile Computing Laboratory": 2,
        "UCS1512 Computer Networks Laboratory": 2,
        "UHS1561 Professional Communication Laboratory": 2,
        "UHS1551 Professional Skills-IV": 1
    },
    "Semester 6": {
        "UCS1601 Data Warehousing and Data Mining": 4,
        "UCS1602 Compiler Design": 4,
        "UCS1603 Object Oriented Analysis and Design": 3,
        "UCS1604 Machine Learning": 4,
        "Professional Elective-II": 3,
        "Open Elective-I": 3,
        "UCS1611 Data Mining Laboratory": 2,
        "UCS1612 Compiler Design Laboratory": 2,
        "UCS1613 Object Oriented Analysis and Design Laboratory": 2
    },
    "Semester 7": {
        "UCS1701 Cloud Computing": 3,
        "UCS1702 Computer Graphics": 3,
        "UCS1703 Data Visualization": 3,
        "UCS1704 Human Computer Interaction": 3,
        "Professional Elective-III": 3,
        "Professional Elective-IV": 3,
        "UCS1711 Cloud Computing Laboratory": 2,
        "UCS1712 Computer Graphics Laboratory": 2
    },
    "Semester 8": {
        "Professional Elective-V": 3,
        "Professional Elective-VI": 3,
        "Open Elective-II": 3,
        "UCS1811 Project Work": 6
    }
}

eee = {
    "Semester 1": {
        "UHS1151 Technical English - I": 3,
        "UMA1151 Mathematics - I": 4,
        "UPH1151 Engineering Physics - I": 3,
        "UCY1151 Engineering Chemistry": 3,
        "UGE1151 Python Programming and Problem Solving": 3,
        "UBE1161 Basic Civil and Mechanical Engineering": 4,
        "UBS1161 Physics and Chemistry Laboratory": 2,
        "UGE1161 Python Programming and Problem Solving Laboratory": 2
    },
    "Semester 2": {
        "UHS1251 Technical English - II": 3,
        "UMA1251 Mathematics - II": 4,
        "UPH1251 Engineering Physics - II": 3,
        "UGE1251 Environmental Science and Engineering": 3,
        "UGE1252 C Programming": 3,
        "UGE1253 Engineering Graphics": 3,
        "UHS1252 Professional skills - I": 1,
        "UBE1261 Basic Electrical and Electronics Engineering": 3,
        "UGE1261 C Programming Laboratory": 2
    },
    "Semester 3": {
        "UMA1352 Transforms and Partial Differential Equations": 4,
        "UEE1301 Electromagnetic Field Theory": 3,
        "UEE1302 Electrical Machines - I": 3,
        "UEE1303 Electron Devices and Circuits": 3,
        "UEE1304 Circuit Theory": 4,
        "UEE1305 Electrical and Electronics Measurements": 3,
        "UHS1351 Professional Skills - II": 1,
        "UEE1311 Electron Devices and Circuits Laboratory": 2,
        "UEE1312 Electrical Machines Laboratory - I": 2,
        "UEE1313 Electric Circuits Laboratory": 2
    },
    "Semester 4": {
        "UMA1451 Numerical Methods and Optimization Techniques": 4,
        "UEE1401 Electrical Machines - II": 3,
        "UEE1402 Transmission and Distribution": 3,
        "UEE1403 Linear Integrated Circuits": 3,
        "UEE1404 Digital Logic Circuits": 3,
        "UEE1405 Power Plant Technology": 3,
        "UHS1451 Professional Skills - III": 1,
        "UEE1411 Electrical Machines Laboratory - II": 2,
        "UEE1412 Linear and Digital Integrated Circuits Laboratory": 2,
        "UHS1361 Interpersonal Skills Laboratory": 1
    },
    "Semester 5": {
        "UEE1501 Control Systems": 4,
        "UEC1551 Microprocessors, Microcontrollers and Applications": 3,
        "UEE1503 Power Electronics": 3,
        "UEC1552 Principles of Digital Signal Processing": 3,
        "UCS1551 Data Structures and Object Oriented Programming": 3,
        "UHS1551 Professional Skills - IV": 1,
        "UEE1511 Control and Instrumentation Laboratory": 2,
        "UEC1561 Microprocessors, Microcontrollers and Applications Laboratory": 2,
        "UCS1561 Data Structures and Object Oriented Programming Laboratory": 2
    },
    "Semester 6": {
        "UEE1601 Power System Analysis": 3,
        "UEE1602 Solid State Drives": 3,
        "UEE1603 Protection and Switchgear": 3,
        "Open Elective - I": 3,
        "Professional Elective - II": 3,
        "Professional Elective - III": 3,
        "UEE1611 Power Electronics and Drives Laboratory": 2,
        "UEE1612 Mini Project": 2,
        "UHS1561 Professional Communication Laboratory": 2
    },
    "Semester 7": {
        "UEE1701 Power System Operation and Control": 3,
        "UEE1702 High Voltage Engineering": 3,
        "UEE1703 Renewable Energy Systems": 3,
        "UMG1054 Professional Ethics in Engineering": 3,
        "Open Elective - II": 3,
        "Professional Elective - IV": 3,
        "UEE1711 Power System Simulation Laboratory": 2,
        "UEE1712 Renewable Energy Systems Laboratory": 2,
        "UEE1713 Technical Seminar": 1
    },
    "Semester 8": {
        "Professional Elective - V": 3,
        "Professional Elective - VI": 3,
        "UEE1811 Project Work": 6
    }
}

ece = {
    "Semester 1": {
        "Technical English - I": 3,
        "Mathematics - I": 4,
        "Engineering Physics - I": 3,
        "Engineering Chemistry": 3,
        "Python Programming and Problem Solving": 3,
        "Basic Civil and Mechanical Engineering": 4,
        "Physics and Chemistry Laboratory": 2,
        "Python Programming and Problem Solving Laboratory": 2
    },
    "Semester 2": {
        "Technical English - II": 3,
        "Mathematics - II": 4,
        "Engineering Physics - II": 3,
        "Environmental Science and Engineering": 3,
        "C Programming": 3,
        "Engineering Graphics": 3,
        "Professional skills - I": 1,
        "Basic Electrical and Electronics Engineering": 3,
        "C Programming Laboratory": 2
    },
    "Semester 3": {
        "Transforms and Numerical Analysis": 4,
        "Circuit Analysis and Devices": 3,
        "Digital Electronics": 3,
        "Signals and Systems": 4,
        "Electronic Circuits": 3,
        "OOPS and Data Structures": 3,
        "Professional Skills-II": 1,
        "Analog and Digital Circuits Laboratory": 2,
        "OOPS and Data Structures Laboratory": 2,
        "Interpersonal Skills Laboratory": 1
    },
    "Semester 4": {
        "Probability and Random Processes": 4,
        "Linear Integrated Circuits and Applications": 3,
        "Microprocessors and Microcontrollers": 3,
        "Electromagnetic Theory": 4,
        "Analog and Digital Communication": 3,
        "Control Systems Engineering": 3,
        "Professional Skills-III": 1,
        "Linear Integrated Circuits Laboratory": 2,
        "Microprocessors and Microcontrollers Laboratory": 2,
        "Analog and Digital Communication Laboratory": 2
    },
    "Semester 5": {
        "Digital Signal Processing": 4,
        "VLSI Design": 3,
        "Transmission Lines and RF Systems": 4,
        "Principles of Management": 3,
        "Computer Architecture": 3,
        "Professional Skills-IV": 1,
        "Digital Signal Processing Laboratory": 2,
        "VLSI Design Laboratory": 2,
        "Professional Communication Laboratory": 2
    },
    "Semester 6": {
        "Antenna and Microwave Measurements": 4,
        "Embedded Systems and IoT": 3,
        "Communication Networks": 3,
        "Speech and Image Processing": 3,
        "Programmable Logic Controller": 3,
        "Professional Elective – I": 3,
        "Embedded Systems and IoT Laboratory": 2,
        "Speech and Image Processing Laboratory": 2
    },
    "Semester 7": {
        "RF MEMS circuit design": 3,
        "Optical Communication Networks": 3,
        "Adhoc and Wireless Sensor Networks": 3,
        "Wireless Communication": 3,
        "Professional Ethics in Engineering": 3,
        "Open Elective - II": 3,
        "RF System Design and Communication Laboratory": 2,
        "Networks Laboratory": 2
    },
    "Semester 8": {
        "Professional Elective - II": 3,
        "Professional Elective - III": 3,
        "Project Work": 6
    }
}

mech = {
    "Semester 1": {
        "UHS1151 Technical English - I": 3,
        "UMA1151 Mathematics - I": 4,
        "UPH1151 Engineering Physics - I": 3,
        "UCY1151 Engineering Chemistry": 3,
        "UGE1151 Python Programming and Problem Solving": 3,
        "UBE1161 Basic Civil and Mechanical Engineering (Theory + Lab)": 4,
        "UBS1161 Physics and Chemistry Laboratory": 2,
        "UGE1161 Python Programming and Problem Solving Laboratory": 2
    },
    "Semester 2": {
        "UHS1251 Technical English - II": 3,
        "UMA1251 Mathematics - II": 4,
        "UPH1251 Engineering Physics - II": 3,
        "UGE1251 Environmental Science and Engineering": 3,
        "UGE1252 C Programming": 3,
        "UGE1253 Engineering Graphics": 3,
        "UHS1252 Professional skills - I": 1,
        "UBE1261 Basic Electrical and Electronics Engineering (Theory + Lab)": 3,
        "UGE1261 C Programming Laboratory": 2
    },
    "Semester 3": {
        "UMA1352 Transforms and Partial Differential Equations": 4,
        "UME1301 Engineering Thermodynamics": 4,
        "UEE1351 Electrical Drives and Controls": 3,
        "UME1302 Fluid Mechanics and Machineries": 4,
        "UME1303 Engineering Mechanics": 4,
        "UHS1351 Professional Skills – II": 1,
        "UEE1361 Electrical Drives and Controls Laboratory": 2,
        "UME1311 Fluid Mechanics and Machineries Laboratory": 2,
        "UME1312 Machine Drawing Laboratory": 2
    },
    "Semester 4": {
        "UMA1452 Statistics, Numerical Methods and Optimization Techniques": 4,
        "UME1401 Production Technology – I": 3,
        "UME1402 Engineering Metallurgy": 3,
        "UME1403 Kinematics of Machinery": 4,
        "UME1404 Strength of Materials": 4,
        "Open Elective – I": 3,
        "UHS1451 Professional Skills – III": 1,
        "UME1411 Production Technology Laboratory - I": 2,
        "UME1412 Strength of Materials Laboratory": 2
    },
    "Semester 5": {
        "UME1501 Thermal Engineering": 4,
        "UME1502 Dynamics of Machinery": 3,
        "UME1503 Design of Machine elements": 4,
        "UME1504 Production Technology – II": 3,
        "UME1505 Hydraulics and Pneumatics": 3,
        "UHS1551 Professional Skills – IV": 1,
        "UME1511 Thermal Engineering Laboratory": 2,
        "UME1512 Dynamics of Machinery Laboratory": 2,
        "UME1513 Production Technology Laboratory - II": 2,
        "UHS1361 Interpersonal Skills Laboratory": 1
    },
    "Semester 6": {
        "UME1601 Design of Transmission systems": 3,
        "UME1602 Finite Element Analysis": 4,
        "UME1603 Heat and Mass Transfer": 4,
        "Professional Elective – I": 3,
        "Professional Elective – II": 3,
        "UME1611 Simulation and Analysis Laboratory": 2,
        "UME1612 Design and Fabrication Laboratory": 2,
        "UME1613 Heat and Mass Transfer Laboratory": 2,
        "UHS1561 Professional Communication Laboratory": 2
    },
    "Semester 7": {
        "UME1701 Mechatronics": 3,
        "UME1702 Industrial Engineering": 3,
        "UME1703 Metrology and Measurements": 3,
        "Open Elective – II": 3,
        "Professional Elective – III": 3,
        "UME1711 Computer Aided Design and Manufacturing": 4,
        "UME1712 Mechatronics Laboratory": 2,
        "UME1713 Metrology and Measurements Laboratory": 2
    },
    "Semester 8": {
        "Professional Elective – IV": 3,
        "Professional Elective – V": 3,
        "UME1811 Project work": 6
    }
}

aids = {
    "Semester 1": {
        "UHS1151 Technical English - I": 3,
        "UMA1151 Mathematics - I": 4,
        "UPH1151 Engineering Physics - I": 3,
        "UCY1151 Engineering Chemistry": 3,
        "UGE1151 Python Programming and Problem Solving": 3,
        "UBE1161 Basic Civil and Mechanical Engineering (Theory + Lab)": 4,
        "UBS1161 Physics and Chemistry Laboratory": 2,
        "UGE1161 Python Programming and Problem Solving Laboratory": 2
    },
    "Semester 2": {
        "UHS1251 Technical English - II": 3,
        "UMA1251 Mathematics - II": 4,
        "UPH1251 Engineering Physics - II": 3,
        "UGE1251 Environmental Science and Engineering": 3,
        "UGE1252 C Programming": 3,
        "UGE1253 Engineering Graphics": 3,
        "UHS1252 Professional skills - I": 1,
        "UBE1261 Basic Electrical and Electronics Engineering (Theory + Lab)": 3,
        "UGE1261 C Programming Laboratory": 2
    },
    "Semester 3": {
        "UMA1353 Linear Algebra and Discrete Mathematics": 4,
        "UEC1353 Analog and Digital Electronics": 3,
        "UAD1301 Data Structures and Algorithm Analysis": 3,
        "UAD1302 Computer Organization and Architecture": 3,
        "UAD1303 Object Oriented Programming": 3,
        "UAD1304 Data Analytics": 3,
        "UHS1351 Professional Skills - II": 1,
        "UEC1363 Analog and Digital Electronics Laboratory": 2,
        "UAD1311 Data Structures and Algorithms Laboratory": 2,
        "UAD1312 Object Oriented Programming Laboratory": 2
    },
    "Semester 4": {
        "UMA1456 Probability and Statistics": 4,
        "UAD1401 Artificial Intelligence - I": 3,
        "UAD1402 Operating System Concepts": 3,
        "UCS1403 Software Engineering": 3,
        "UAD1403 Database Design and Management": 3,
        "UAD1404 Fundamentals of Data Science": 4,
        "UHS1451 Professional Skills – III": 1,
        "UAD1411 Fundamentals of Data Science Laboratory": 2,
        "UAD1412 Database Design and Management Laboratory": 2,
        "UHS1361 Interpersonal Skills Laboratory": 1
    },
    "Semester 5": {
        "UAD1501 Artificial Intelligence - II": 3,
        "UAD1502 Data Communications and Networking": 3,
        "UAD1503 Optimization Techniques": 3,
        "UAD1504 Data Mining and Visualization": 3,
        "UAD1505 Machine Learning Techniques": 4,
        "Professional Elective I": 3,
        "UHS1551 Professional Skills – IV": 1,
        "UAD1511 Machine Learning Techniques Laboratory": 2,
        "UAD1512 Data Mining and Visualization Laboratory": 2,
        "UAD1581 MOOC Certificate Course": 0
    },
    "Semester 6": {
        "UAD1601 Web Technology": 3,
        "UAD1602 Big Data Technologies": 3,
        "UAD1603 Computer Vision": 3,
        "UAD1604 Data and Information Security": 3,
        "Professional Elective – II": 3,
        "Professional Elective – III": 3,
        "UAD1611 Web Technology Laboratory": 2,
        "UAD1612 Big Data Technologies Laboratory": 2,
        "UHS1561 Professional Communication Laboratory": 2,
        "UAD1691 Yoga for Health Care": 0
    },
    "Semester 7": {
        "UAD1701 Deep Learning Techniques": 4,
        "UAD1702 Internet of Things": 3,
        "UAD1703 Streaming Analytics": 3,
        "Professional Elective – IV": 3,
        "Open Elective – I": 3,
        "UAD1711 Deep Learning Techniques Laboratory": 2,
        "UAD1712 Project Phase - I": 4
    },
    "Semester 8": {
        "UAD1801 Information Retrieval": 3,
        "Professional Elective – V": 3,
        "Open Elective – II": 3,
        "UAD1811 Project Phase - II": 6
    }
}

csai = {
    "Semester 1": {
        "UHS1151 Technical English - I": 3,
        "UMA1151 Mathematics - I": 4,
        "UPH1151 Engineering Physics - I": 3,
        "UCY1151 Engineering Chemistry": 3,
        "UGE1151 Python Programming and Problem Solving": 3,
        "UBE1161 Basic Civil and Mechanical Engineering (Theory + Lab)": 4,
        "UBS1161 Physics and Chemistry Laboratory": 2,
        "UGE1161 Python Programming and Problem Solving Laboratory": 2
    },
    "Semester 2": {
        "UHS1251 Technical English - II": 3,
        "UMA1251 Mathematics - II": 4,
        "UPH1251 Engineering Physics - II": 3,
        "UGE1251 Environmental Science and Engineering": 3,
        "UGE1252 C Programming": 3,
        "UGE1253 Engineering Graphics": 3,
        "UHS1252 Professional skills - I": 1,
        "UBE1261 Basic Electrical and Electronics Engineering (Theory + Lab)": 3,
        "UGE1261 C Programming Laboratory": 2
    },
    "Semester 3": {
        "UMA1353 Linear Algebra and Discrete Mathematics": 4,
        "UAM1301 Design and Analysis of Algorithms": 3,
        "UEC1352 Digital Principles and Systems Design": 3,
        "UAM1302 Data Structures in Python": 3,
        "UAD1303 Object Oriented Programming": 3,
        "UAD1302 Computer Organization and Architecture": 3,
        "UHS1351 Professional Skills - II": 1,
        "UEC1362 Digital Principles and Systems Design Laboratory": 2,
        "UAM1311 Data Structures in Python Laboratory": 2,
        "UAD1312 Object Oriented Programming Laboratory": 2
    },
    "Semester 4": {
        "UMA1456 Probability and Statistics": 4,
        "UAM1401 Machine Learning – I": 3,
        "UAD1401 Artificial Intelligence – I": 3,
        "UAD1402 Operating System Concepts": 3,
        "UCS1403 Software Engineering": 3,
        "UAD1403 Database Design and Management": 3,
        "UHS1451 Professional Skills – III": 1,
        "UAM1411 Machine Learning - I Laboratory": 2,
        "UAD1412 Database Design and Management Laboratory": 2,
        "UHS1361 Interpersonal Skills Laboratory": 1
    },
    "Semester 5": {
        "UAD1501 Artificial Intelligence – II": 3,
        "UAD1502 Data Communications and Networking": 3,
        "UAD1503 Optimization Techniques": 3,
        "UAM1501 Machine Learning – II": 4,
        "UAM1502 Data Mining and Analytics": 3,
        "Professional Elective I": 3,
        "UHS1551 Professional Skills – IV": 1,
        "UAM1511 Machine Learning – II Laboratory": 2,
        "UAM1512 Data Mining and Analytics Laboratory": 2,
        "UAD1581 MOOC Certificate Course": 0
    },
    "Semester 6": {
        "UAD1601 Web Technology": 3,
        "UAM1601 Big Data Management": 3,
        "UAM1602 Data Exploration and Visualization": 3,
        "UAM1603 Health Care Analytics": 3,
        "Professional Elective – II": 3,
        "Professional Elective – III": 3,
        "UAD1611 Web Technology Laboratory": 2,
        "UAM1611 Data Visualization Laboratory": 2,
        "UHS1561 Professional Communication Laboratory": 2,
        "UAD1691 Yoga for Health Care": 0
    },
    "Semester 7": {
        "UAD1701 Deep Learning Techniques": 4,
        "UAM1701 Artificial Intelligence and Robotics": 4,
        "UAD1005 Natural Language Processing": 3,
        "Professional Elective – IV": 3,
        "Open Elective – I": 3,
        "UAD1711 Deep Learning Techniques Laboratory": 2,
        "UAM1711 Project Phase - I": 4
    },
    "Semester 8": {
        "UCS1020 Software Project Management": 3,
        "Professional Elective – V": 3,
        "Open Elective – II": 3,
        "UAM1811 Project Phase - II": 6
    }
}

it = {
    "Semester 1": {
        "UHS1151 Technical English - I": 3,
        "UMA1151 Mathematics - I": 4,
        "UPH1151 Engineering Physics - I": 3,
        "UCY1151 Engineering Chemistry": 3,
        "UGE1151 Python Programming and Problem Solving": 3,
        "UBE1161 Basic Civil and Mechanical Engineering (Theory + Lab)": 4,
        "UBS1161 Physics and Chemistry Laboratory": 2,
        "UGE1161 Python Programming and Problem Solving Laboratory": 2
    },
    "Semester 2": {
        "UHS1251 Technical English - II": 3,
        "UMA1251 Mathematics - II": 4,
        "UPH1251 Engineering Physics - II": 3,
        "UGE1251 Environmental Science and Engineering": 3,
        "UGE1252 C Programming": 3,
        "UGE1253 Engineering Graphics": 3,
        "UHS1252 Professional skills - I": 1,
        "UBE1261 Basic Electrical and Electronics Engineering (Theory + Lab)": 3,
        "UGE1261 C Programming Laboratory": 2
    },
    "Semester 3": {
        "UMA1351 Discrete Mathematics and Graph Theory": 4,
        "UEC1352 Digital Principles and Systems Design": 3,
        "UIT1301 Data Structures and Algorithm Analysis": 3,
        "UIT1302 Computer Organization and Architecture": 3,
        "UIT1303 Object Oriented Programming": 3,
        "UHS1351 Professional Skills-II": 1,
        "UIT1311 Data Structures and Algorithms Laboratory": 2,
        "UIT1312 Object Oriented Programming Laboratory": 2,
        "UEC1362 Digital Principles and Systems Design Laboratory": 2
    },
    "Semester 4": {
        "UMA1456 Probability and Statistics": 4,
        "UIT1401 Database Systems": 3,
        "UCS1402 Operating Systems": 3,
        "UIT1402 Web based Internet Programming": 3,
        "UIT1403 Introduction to Artificial Intelligence": 3,
        "UHS1451 Professional Skills-III": 1,
        "UIT1411 Database Management Systems Laboratory": 2,
        "UIT1412 Internet Programming Laboratory": 2,
        "UHS1361 Interpersonal Skills Laboratory": 1,
        "UIT1413 Mini Project": 2
    },
    "Semester 5": {
        "UCS1403 Software Engineering": 3,
        "UIT1501 Computer Network Fundamentals": 3,
        "UEC1402 Microprocessors and Microcontrollers": 3,
        "UIT1502 Mobile Application Development": 3,
        "UIT1503 Data Mining Techniques": 3,
        "Professional Elective-I": 3,
        "UHS1551 Professional Skills-IV": 1,
        "UIT1511 Computer Networks Laboratory": 2,
        "UIT1512 Mobile Application Development Laboratory": 2,
        "UEC1412 Microprocessors and Microcontrollers Laboratory": 2
    },
    "Semester 6": {
        "UIT1601 Object Oriented Modelling": 3,
        "UIT1602 Big Data Analytics": 3,
        "UIT1603 Information Storage and Management": 3,
        "UIT1604 Computer Graphics and Multimedia": 3,
        "Professional Electives-II": 3,
        "Open Elective-I": 3,
        "UIT1611 Object Oriented Modelling Laboratory": 2,
        "UIT1612 Data Analytics Laboratory": 2,
        "UIT1613 Computer Graphics and Multimedia Laboratory": 2,
        "UHS1561 Professional Communication Laboratory": 2
    },
    "Semester 7": {
        "UIT1701 Cloud Computing": 4,
        "UIT1702 Network Security": 4,
        "UIT1703 Internet of Things Architecture and protocols": 4,
        "Professional Elective -III": 3,
        "Professional Elective-IV": 3,
        "UIT1711 Cloud Computing Laboratory": 2,
        "UIT1712 Network Security Laboratory": 2,
        "UIT1713 Internet Computing Laboratory": 2
    },
    "Semester 8": {
        "Professional Elective-V": 3,
        "Professional Elective-VI": 3,
        "Open Elective-II": 3,
        "UIT1811 Project Work": 6
    }
}


