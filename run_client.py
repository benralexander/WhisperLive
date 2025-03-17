import argparse
import traceback
import whisper_live.programmatic_state_test
from whisper_live.client import TranscriptionClient
from whisper_live.utils import confirm_device_index_acceptable_as_microphone,confirm_host_is_desirable


def main_client(args,host:str,input_index:int):
    try:
        # while True:
        transcription_client = TranscriptionClient(host=host,
                                                   port=args.port,
                                                   device_index=input_index,
                                                   )
        transcription_client()
    except Exception as e:
        traceback_info = traceback.format_exc()
        print(traceback_info)

def arg_parser()->argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p',
                        type=int,
                        default=9090,
                        help="Websocket port to run the server on.")
    parser.add_argument('--server', '-s',
                        type=str,
                        required= False,
                        help="Host for the server.")
    parser.add_argument('--device_index', '-dv',
                        type=int,
                        default=4,
                        help="Device index")
    parser.add_argument('--programmer_mode', '-pm',
                        action='store_true',
                        help="Use this as a programmer might, not for transcription purposes")
    parser.add_argument('--log_level', '-l',
                        type=str,
                        default="INFO",
                        required=False,
                        help="Host for the server.")


if __name__ == "__main__":
    args = arg_parser()
    if args.foo:
        whisper_live.programmatic_state_test.run_unit_tests()
    else:
        host=confirm_host_is_desirable(args.server)
        input_index=confirm_device_index_acceptable_as_microphone(args.device_index)
        main_client(args,host,input_index)