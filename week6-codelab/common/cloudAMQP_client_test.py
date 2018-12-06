from cloudAMQP_client import CloudAMQPClient

TEST_CLOUDAMQP_URL = "amqp://gzoyqqhz:_oxwWZ9NDHUMr2boFcKUCRvchsgGzlo7@clam.rmq.cloudamqp.com/gzoyqqhz"
TEST_QUEUE_NAME = "test"

def test_basic():
    client = CloudAMQPClient(TEST_CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {'test':'test'}
    client.sendMessage(sentMsg)

    client.sleep(5)

    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg

    print('test_basic passed.')

if __name__ == "__main__":
    test_basic()