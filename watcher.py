"""Watches a ticket on TicketSwap"""
from optparse import OptionParser

from ticketswap.monitor import TicketSwapMonitor
from ticketswap.logger import Logger

if __name__ == '__main__':
    usage = "usage: %prog [options] url"
    parser = OptionParser(usage=usage)
    parser.add_option("-u", "--user", dest="user",
                      help="Facebook username", metavar="USER")
    parser.add_option("-p", "--password", dest="password",
                      help="Facebook password", metavar="PASSWORD")
    parser.add_option("-f", "--credentials-file", dest="file",
                      help="File with credentials", metavar="FILE")
    parser.add_option("-l", "--limit", dest="limit", default=10,
                      help="Max limit", metavar="LIMIT")

    (options, args) = parser.parse_args()

    monitor = TicketSwapMonitor(args[0], options)
    monitor.set_logger(Logger())
    monitor.run()
