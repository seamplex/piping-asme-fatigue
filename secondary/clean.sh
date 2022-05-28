if [ -d results ] ; then
  mv results results-`date +%F_%T`
fi
cat .gitignore | sed '/^#.*/ d' | sed '/^\s*$/ d' | sed 's/^/rm -rf /' | bash
rm -f mech.msh ../mech.msh
