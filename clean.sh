# from https://stackoverflow.com/questions/13541615/how-to-remove-files-that-are-listed-in-the-gitignore-but-still-on-the-repositor
cat .gitignore | grep -v cad | grep -v old | sed '/^#.*/ d' | sed '/^\s*$/ d' | sed 's/^/rm -rf /' | bash

for i in transients thermal primary modal secondary fatigue; do
  cd $i
  ./clean.sh
  cd ..
done

