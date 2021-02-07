from msg_parser import MsOxMessage

class MsgConvert:

    def msg_to_eml(self, msg):
        msg_obj = MsOxMessage(msg)
        save_path = msg_obj.save_email_file('emails/')
        return f'Converted {msg} successfully.'