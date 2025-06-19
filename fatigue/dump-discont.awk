BEGIN {
 n = 1;
}
{
 if (n != $2) {
   print $1
   n = $2
 }
}
