{
  printf("\\subfloat[$f_{%d}=\\SI{%.1f}{\\hertz}$]{\\href{mode%d.webm}{\\xbox{\\includegraphics[width=0.33\\linewidth]{mode%d.png}}}}%s\n",
         $1, $2, $1, $1, ($1 % 3 == 0)?"\\\\":"");
}
