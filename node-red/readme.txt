node-red �� csv���J�����@			2019/7/6

[�ړI]
Node-red �̓f�t�H���g�ł́A�摜���܂߂āA�R���s���[�^���
�f�[�^��ǂݍ��ނ��Ƃ��ł��܂���B
���̂��߁A���[�J���f�B���N�g����ǂݍ��߂�悤��
�ύX����K�v������܂��B
# �����CSV��ǂݍ��ނ��߂ɑ��삵�Ă��܂����A
# �摜����Node-red�œǂ݂����ꍇ���ꏏ�ł��B


[�菇]
1. Node-red ���C���X�g�[������Ă���f�B���N�g���Ɉړ�
�iRaspbian �Ȃ��) /home/pi/.node-red/
 (Windows  �Ȃ��) C:\Users\WASEDA\.node-red\

2. settings.js ��ҏW
  ��L�f�B���N�g������ settings.js �����邽�߁A�e�L�X�g�G�f�B�^���ŊJ���B
  106�s�ڂ����肩��A�ȉ��̋L�ڂ�����̂ŁA"//" ���O���ėL�������A
  csv�t�@�C�����i�[����ꏊ���w�肵�܂��B
  -------
    // When httpAdminRoot is used to move the UI to a different root path, the
    // following property can be used to identify a directory of static content
    // that should be served at http://localhost:1880/.
��  httpStatic: 'C:/Users/WASEDA/.node-red/node-red-static/',
  -------
  �� �����ł� .node-red �z���� node-red-static �Ƃ����f�B���N�g����
     �쐬���Ă����� csv ���i�[

3. node-red ���ċN��
   node-red ���N�����Ă���ꍇ�́A�ċN������B

4. node-red �̏C��
   Result��ʂ̃m�[�h�ŁA�t�@�C���p�X���w�肵�Ă���ӏ������邽�߁A
   csv���i�[���Ă���Path�ɏC������
   
   [�t�@�C���p�X���L��] �m�[�h���J���Acsv �̊i�[�ꏊ���΃p�X�Ŏw�肷��
   C:/Users/WASEDA/.node-red/node-red-static/test.csv
   
   
�ȏ�
