/*
// Sample code to perform I/O:

val name = scala.io.StdIn.readLine()        // Reading input from STDIN
println("Hi, " + name + ".")                // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
import scala.collection.mutable.ListBuffer
/**
 *
 * Binary Search
 */
object MarbelBoxNumber extends App {
  def find(nums:List[Int], start:Int, ending:Int, key:Int): Int =
  {
    val mid:Int =(start+ending)/2
    if (start> ending){
      return start
    }
    if(nums(mid)==key) return mid
    else if(nums(mid)<key) return find(nums,mid+1,ending,key)
    else if(nums(mid)>key) return find(nums,start,mid-1,key)
    mid
  }


  val numberOfBoxes=scala.io.StdIn.readLine().toInt
  val listOfMarblesInBoxes=scala.io.StdIn.readLine().split(' ').map(_.trim).toList.map((s: String) =>s.toInt)
  val numOfQueries=scala.io.StdIn.readLine().toInt
  var bufferList = new ListBuffer[Int]()
  listOfMarblesInBoxes.zipWithIndex.foreach{ case (e, i) => val x:Int=if(i!=0){bufferList(i-1)+e}else e;bufferList+=x}
  val listMarbles=bufferList.toList
  //println(listMarbles)
  for(i <- 1 to numOfQueries)
  {
    val keyToBeFound=scala.io.StdIn.readLine().toInt
    println(find(listMarbles,0,numberOfBoxes-1,keyToBeFound)+1)
  }
  //println(listMarbles)
}