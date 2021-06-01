package HackerEarth.Leonteq_Challange

import scala.collection.mutable

object KopsMinSum extends App {
  val inputStr: Array[String] ="5 2".split(' ')//scala.io.StdIn.readLine().split(" ")
  val listLen: Int =inputStr(0).toInt
  var kOps: Int =if (inputStr(1).toInt > listLen/2) listLen/2 else inputStr(1).toInt
  val strInputList="5 5 5 5 5"//scala.io.StdIn.readLine()
  val pq: mutable.PriorityQueue[Long] = scala.collection.mutable.PriorityQueue[Long]()
  strInputList.split(' ').map(_.trim).toList.map((s: String) => pq.enqueue(s.toLong))

  for (i <- 1 to kOps) {
    val x= pq.dequeue()
    pq.enqueue((x / 2.00).ceil.toInt)
  }
  val sortedQ: Seq[Long] = pq.clone.dequeueAll.sortWith(_ < _)
  var tempK=0
  var result:Long=0
  sortedQ.foreach(dqElem =>
    if (tempK<kOps){
      tempK+=1
      result=result+(dqElem*2)
    }
    else
      result=result+dqElem
  )
  println(result)
}
