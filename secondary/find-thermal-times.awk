{
  if (t < $1) {
    print last, $1;
    exit;
  }
  last = $1;
}
