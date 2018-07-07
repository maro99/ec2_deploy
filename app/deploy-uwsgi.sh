#!/usr/bin/env bash

IDENTITY_FILE="$HOME/.ssh/fc-8th.pem"
USER="ubuntu"
HOST="ec2-13-124-210-106.ap-northeast-2.compute.amazonaws.com"
PROJECT_DIR="$HOME/Desktop/projects/deploy/ec2-deploy"
SERVER_DIR="/home/ubuntu/project"

# ssh로 서버에 접속하는 명령어
CMD_CONNECT="ssh -i ${IDENTITY_FILE} ${USER}@${HOST}"

#서버에서 실행중이던  uwsgi 프로세스들을 모두 종료
${CMD_CONNECT} "pkill -9 -ef uwsgi"
echo "kill  uwsgi process"


# 서버의 파일을 지움.
${CMD_CONNECT} rm -rf ${SERVER_DIR}
echo "-Delete server files"


# 서버에 프로젝트 파일을 다시 업로드.
scp -q -i ${IDENTITY_FILE} -r ${PROJECT_DIR} ${USER}@${HOST}:${SERVER_DIR}
echo "-Upload files"


# 서버 접속 후 SERVER_DIR로 이동, pipenv --venv로 가상환경의 경로 가져오기
VENV_PATH=$(${CMD_CONNECT} "cd ${SERVER_DIR} && pipenv --venv")
## 가상환경의 경로에 /bin/python을 붙여 서버에서 사용하는 python의 경로 만들기
#PYTHON_PATH="${VENV_PATH}/bin/python"
#echo "=GET Python path ($PYTHON_PATH)"


# runserver를 background에서 실행해주는 커맨드 (nohup)

RUNSERVER_CMD="nohup ${VENV_PATH}/bin/uwsgi --ini .config/uwsgi_http2.ini &>/dev/null &"
#서버 좁속 후, 프로젝트의 'app'폴더까지 이동한후 runserver 명령어를 실행
${CMD_CONNECT} "cd ${SERVER_DIR} && ${RUNSERVER_CMD}"
echo  "Execute runserver"

echo "Deploy complete"