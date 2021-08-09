DB_NAME = 'cricket'

TABLES = {}

TABLES['match_data'] = (
    "CREATE TABLE `match_data` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `player` varchar(14) NOT NULL,"
    "  `scored` int NOT NULL,"
    "  `faced` int NOT NULL,"
    "  `fours` int NOT NULL,"
    "  `sixes` int NOT NULL,"
    "  `bowled` int NOT NULL,"
    "  `maiden` int NOT NULL,"
    "  `given` int NOT NULL,"
    "  `wkts` int NOT NULL,"
    "  `catches` int NOT NULL,"
    "  `stumping` int NOT NULL,"
    "  `ro` int NOT NULL,"
    "  PRIMARY KEY (`id`)"    
    ") ENGINE=InnoDB")

TABLES['teams'] = (
    "CREATE TABLE `teams` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(40) NOT NULL,"
    "  `players` varchar(1000) NOT NULL,"
    "  `value` int NOT NULL,"
    "  PRIMARY KEY (`id`), UNIQUE KEY `team_name` (`name`)"
    ") ENGINE=InnoDB")

TABLES['stats'] = (
    "CREATE TABLE `stats` ("
    "  `id` int NOT NULL AUTO_INCREMENT,"
    "  `player` varchar(40) NOT NULL,"
    "  `matches` int NOT NULL,"
    "  `runs` int NOT NULL,"
    "  `100s` int NOT NULL,"
    "  `50s` int NOT NULL,"
    "  `value` int NOT NULL,"
    "  `ctg` varchar(3) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
