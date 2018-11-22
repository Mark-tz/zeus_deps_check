if [ -z "$1" ]; then
    echo 'usage: auto rootpath'
    exit 1
else
	echo 'rootpath : $1'
fi
ZROOT=$1 python3 cpp_deps.py > cdeps.txt
ZROOT=$1 python3 cpp_r1.py > cr1.txt
ZROOT=$1 python3 cpp_r2.py > cr2.txt
ZROOT=$1 python3 cpp_r3.py > cr3.txt
ZROOT=$1 python3 cpp_r.py > cr.txt
ZROOT=$1 python3 final.py > final.dot
dot -Tsvg final.dot -o final.svg

ZROOT=$1 python3 lua_r0.py > lr0.txt
ZROOT=$1 python3 lua_r1.py > lr1.txt
ZROOT=$1 python3 lua_r2.py > lr2.txt
ZROOT=$1 python3 lua_r3.py > lr3.txt
ZROOT=$1 python3 lua_r4.py > lr4.txt
ZROOT=$1 python3 lua_final.py > lf.dot
dot -Tsvg lf.dot -o lf.svg
