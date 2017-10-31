from errbot import BotPlugin, botcmd

class AutoSys(BotPlugin):
    """Example AutoSys plugin for Errbot"""

    @botcmd
    def job_status(self, msg, args):
        """Output job status"""
	return "Test"
