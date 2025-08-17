
function uinstall {
rm -rf /usr/share/chcursor
rm -rf /usr/share/mywal
rm  /usr/bin/chcursor
rm  /usr/bin/mywal
}

function useruinstall {
rm -rf $HOME/.local/share/chcursor
rm -rf $HOME/.local/share/mywal
rm  $HOME/.local/bin/chcursor
rm  $HOME/.local/bin/mywal
}


for param in "$@"
do
case "$param" in
    "--user")
    useruinstall
    exit 0
    ;;
esac
done

uinstall 
exit 0