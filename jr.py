from errbot import BotPlugin, botcmd

class AutoSys(BotPlugin):
    """Example AutoSys plugin for Errbot."""

    @botcmd
    def jr(self, msg, args):
        """Output job status"""
	      return "Job Name                                                         Last Start           Last End             ST Run/Ntry Pri/Xit" +
"\n________________________________________________________________ ____________________ ____________________ __ ________ _______" +
"\nAZ7#cmd#UIHealthCheckCMD                                         10/28/2017 22:35:03  10/28/2017 22:35:52  SU 157897088/1 0"
