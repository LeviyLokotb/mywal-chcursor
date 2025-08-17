#!/bin/bash
##################
function install {
echo "Копирование файлов в систему..."
mywal_dir="/usr/share/mywal"
chcursor_dir="/usr/share/chcursor"
mkdir -p $mywal_dir
mkdir -p $chcursor_dir
cp -r ./chcursor/*  $chcursor_dir
cp -r ./mywal/* $mywal_dir

echo "Создание виртуального окружения python для mywal..."
mywal_venv="$mywal_dir/.venv"
python3 -m venv "$mywal_venv"
source "$mywal_nenv/bin/activate"
pip install -r "$mywal_dir/requirements.txt"
deactivate

echo "Создание виртуального окружения python для chcursor..."
chcursor_venv="$chcursor_dir/.venv"
python3 -m venv "$chcursor_venv"
source "$chcursor_venv/bin/activate"
pip install -r "$chcursor_dir/requirements.txt"
deactivate

echo "Добавление скриптов запуска..."
mywal_bin="/usr/bin/chcursor"
chcursor_bin="/usr/bin/mywal"
touch $mywal_bin
chmod 555 $mywal_bin
touch $chcursor_bin
chmod 555 $chcursor_bin
echo -e "#!/bin/bash \\n$chcursor_venv/bin/python3 $chcursor_dir/compare.py" > $chcursor_bin
echo -e "#!/bin/bash \\n$mywal_venv/bin/python3 $mywal_dir/app.py \$*" > $chcursor_bin

echo "INSTALL SUCCESSFULLY!"
exit 0
}
######################
function userinstall {
echo "Копирование файлов в систему..."
mywal_dir="$HOME/.local/share/mywal"
chcursor_dir="$HOME/.local/share/chcursor"
mkdir -p $mywal_dir
mkdir -p $chcursor_dir
cp -r ./chcursor/*  $chcursor_dir
cp -r ./mywal/* $mywal_dir

echo "Создание виртуального окружения python для mywal..."
mywal_venv="$mywal_dir/.venv"
python3 -m venv "$mywal_venv"
source "$mywal_venv/bin/activate"
pip install -r "$mywal_dir/requirements.txt"
deactivate

echo "Создание виртуального окружения python для chcursor..."
chcursor_venv="$chcursor_dir/.venv"
python3 -m venv "$chcursor_venv"
source "$chcursor_venv/bin/activate"
pip install -r "$chcursor_dir/requirements.txt"
deactivate

echo "Добавление скриптов запуска..."
mywal_bin="$HOME/.local/bin/chcursor"
chcursor_bin="$HOME/.local/bin/mywal"
mkdir -p "$HOME/.local/bin/"
touch $mywal_bin
chmod 755 $mywal_bin
touch $chcursor_bin
chmod 755 $chcursor_bin
echo -e "#!/bin/bash \\n$chcursor_venv/bin/python3 $chcursor_dir/compare.py" > $chcursor_bin
echo -e "#!/bin/bash \\n$mywal_venv/bin/python3 $mywal_dir/app.py \$*" > $chcursor_bin

if [[ -z $(grep -i "export PATH=\"\$PATH:\$HOME/.local/bin/\"" $HOME/.bashrc) ]] then
ehco "Добавление .local/bin/ в PATH..."
echo "export PATH=\"\$PATH:\$HOME/.local/bin/\"" >> "$HOME/.bashrc"
fi
echo "INSTALL SUCCESSFULLY!"
exit 0
}
##################
for param in "$@"
do
case "$param" in
    "--user")
    userinstall
    exit 0
    ;;
esac
done

install 
exit 0