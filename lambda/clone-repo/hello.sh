function handler () {
    EVENT_DATA=$1
  
    cd /mnt/efs
    git clone https://github.com/kumarahul98/k3d.git rahul-kumar-test

    RESPONSE="{\"statusCode\": 200, \"body\": \"downloaded successfully\"}"
    echo $RESPONSE
}
