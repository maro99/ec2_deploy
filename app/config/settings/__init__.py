# settings.base
# 모든 설정 모듈 공통사항

# settings.local
# runserver용

# settings.dev
#  RDS, S3을 사용 DEbug메시지 출력

# sttings,production
#   배포용 설정. Debug메시지 출력 안함.
from .local import *