#include<iostream>
#include<algorithm>
#include<string>

using namespace std;





////	////	////	////	start configuring	////	////	/////	////
// please dont change it.




int stepCount;
int enemyFound;
int lastActionTakenByThePlayer;
int numberOfTilesInTheVision;
int vision;
int bombDelay;
int maxBombRange;
int deadzoneStartingStep;
int deadzoneExpansionDelay;
int maxStep;


int** tiles;
/*********************		gameMap		**********************/



class gameMap
{
public:
	gameMap();
	~gameMap();
	int height;
	int width;

private:
	

};

gameMap::gameMap()
{
}

gameMap::~gameMap()
{
}






/*********************		playerClass		**********************/


class playerClass
{
public:
	playerClass();
	~playerClass();
	int x;
	int y;
	int health;
	int bombRange;
	int mineCount;
	int healthUpgradeCount;
	int trapCount;

private:
	
};

playerClass::playerClass()
{
}

playerClass::~playerClass()
{
}

gameMap map;
playerClass player;
playerClass otherPlayer;



int gotoTile(int x,int y)
{
	if (player.x == x && player.y == y)
	{
		cerr << "stay" << endl;
		return 4;
	}
	else if (player.x > x)
	{
		cerr << "left (y kam mishe)" << endl;
		//left (y kam mishe)
		return 0;
	}
	else if (player.x < x)
	{
		cerr << "right (y ziad mishe)" << endl;
		//right (y ziad mishe)
		return 1;
	}
	else if (player.y > y)
	{
		cerr << "up (x kam misheh)" << endl;
		//up (x kam misheh)
		return 2;
	}
	else if (player.y < y)
	{
		cerr << "down (x ziad misheh)" << endl;
		//down (x ziad misheh)
		return 3;
	}
	else
	{
		cerr << "stay" << endl;
		//stay
		return 4;
	}
}


int main()
{
	
	string init;
	cin >> init;
	cin >> map.height >> map.width >> player.x  >> player.y >> player.health >> player.bombRange >> player.trapCount >> vision >> bombDelay >> maxBombRange >> deadzoneStartingStep >> deadzoneExpansionDelay >> maxStep;
	cout << "init confirm" <<endl;
	
	tiles = new int* [map.height];
	for (int i = 0; i < map.height; ++i)
	{
		tiles[i] = new int[map.width];
	}

	cerr << "tol naghsheh : " << map.width << " ertefa naghsheh: " << map.height << endl;
	
	while (1)
	{

		cin >> stepCount >> lastActionTakenByThePlayer >> player.x >> player.y >> player.health >> player.healthUpgradeCount >> player.bombRange >> player.trapCount >> enemyFound;
		
		
		
		if (enemyFound)
		{
			cin >> otherPlayer.x >> otherPlayer.y >> otherPlayer.health;
		}

		cin >> numberOfTilesInTheVision;
		for (int i = 0; i < numberOfTilesInTheVision; i++)
		{
			int x, y, state;
			cin >> x >> y >> state;
			tiles[x][y] = state;
		}
		string EOM;
		cin >> EOM;

		/////////////////////////////////////////////////////////////////////////////////////////
		// :: START CODING FROM HERE :: //
		//cerr << "salam" << endl;
		//nokteh
		cerr << "x: " << player.x << " y: " << player.y << endl;
		cout << gotoTile(map.width / 2, map.height / 2) << endl;
		





	}
	

	return 0;
}
