## These are the questions I was tasked to complete for the take home test


All the implementation are done with python. Though the questions can be implemented with another language I chose to go with python as a python Dev was needed.



####  Problem 1: String transformation (Python, JS)

You are given a string S composed of characters A to Z, formulate a function that transforms a given string by changing each letter as follows: �a� becomes �z�, �b� becomes �y�, �c� becomes �x�, e.t.c

##### Sample input
`>> S = �acdz�`

##### Sample output
`>> zxwa`



#### Problem 2: String splitting (Python, JS)

You a given a string S of any length, formulate a function that splits the strings into substrings of a given length N and returns the substrings in a list. If the length of S is not evenly divisible by N, it is acceptable to have the last substring with a length less than N, see example below.

##### Sample input
```
>> S = �This is a test�

>> N = 3

```

##### Sample output
`>> [�Thi�, �s i�, �s a�, � te�, �st�]`




#### Problem 3: Ceiling alarm (Python, JS)

Assume you have a sensor that reports temperature readings periodically. The readings are stored as 2 lists of equal length; List T composed of timestamps for each reading and list R composed of temperature readings for each of the matching timestamps. Your goal is to identify timestamps at which a certain threshold temperature Q was crossed.

Formulate a function that takes lists T and R and a threshold temperature Q and returns a list of timestamps where Q was exceeded. Note that you should only return timestamps representing a datapoint that crosses the threshold, and ignore those that remain above the threshold.

##### Sample input:
```
>> T =  [1460545900, 1460545910, 1460545920, 1460545930, 1460545940, 1460545950]

>> R = [0, 7, 12, 18, 8, 17]

>> Q = 10

```

##### Sample output
`>> [1460545920, 1460545950]`




#### Problem 4: Stock buying (Python, JS)

You are given a list P of average share prices for a particular stock for each day in a given year. Your goal is to buy 1 share and later sell it at maximum profit. Formulate a function that takes list P and returns the best day to buy (B) and the best day to sell (S). You have to buy the share before you can later sell it.


##### Sample input
`>> P = [30, 20, 10, 15, 17, 25, 20, 23]`

##### Sample output
```
>> B = 3 // buy at price 10

>> S = 6 // sell at price 25

```




##### Problem 5: Bounce the ball

Please see the code below which moves a ball through 2D space. You may use and edit *either* the Python or Java code below, whichever you are more comfortable with.

This code defines a wall, but currently allows the ball to pass through it.

Please adjust the code so that the ball bounces back if it contacts the vertical wall.  Ignore physics (friction, gravity, etc).

Please copy the code into your answer, and adjust as you see fit.



```
WALL_X = 5 # A vertical line on a 2D coordinate system at x = 5

class Ball(object):
    
    def __init__(self, _vx=0.5, _vy=0.5):
        self.running = False
        self.x = 0 # Position X
        self.y = 0 # Position Y
        self.vx = _vx # Velocity X
        self.vy = _vy # Velocity Y

    def step(self):
        self.x += self.vx
        self.y += self.vy
        print "Stepped to %s, %s" % (this.x, this.y)

    def run(self, steps=50):
        if not self.running:
            self.running = True
            for s in range(steps):
                self.step()
            self.running = False


b = Ball()
b.run()

```


##### Java

```
public class Ball {

    public static int WALL_X = 5; // A vertical line on a 2D coordinate system at x = 5

    private double x;
    private double y;
    private double vx;
    private double vy;
    private boolean running;


    public Ball(double _vx, double _vy) {
        this.running = false;
        this.x = 0; // Position X
        this.y = 0; // Position Y
        this.vx = _vx; // Velocity X
        this.vy = _vy; // Velocity Y
    }

    private void step() {
        this.x += this.vx;
        this.y += this.vy;
        System.out.println("Stepped to " + this.x + ", " + this.y);
    }

    public void run( int steps ) {
        if (!this.running) {
            this.running = true;
            for (int i=0; i<steps; i++) {
            this.step();
            }
            this.running = false;
        }
    }

    public static void  main(String[] args){        
        Ball b = new Ball(0.5, 0.5);
        b.run(50);
    }
}
