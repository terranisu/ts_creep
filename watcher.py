"""Watches a ticket on ticketswap.com"""

from optparse import OptionParser
from ticketswap.monitor import Monitor as TicketSwapMonitor
from ticketswap.logger import Logger as TicketSwapLogger

if __name__ == "__main__":
    usage = "usage: %prog [options] url"
    parser = OptionParser(usage=usage)
    parser.add_option("-u", "--user", dest="user",
                      help="Facebook username", metavar="USER")
    parser.add_option("-p", "--password", dest="password",
                      help="Facebook password", metavar="PASSWORD")
    parser.add_option("-n", "--phone-number", dest="phone",
                      help="Phone number", metavar="Number")
    parser.add_option("-f", "--settings-file", dest="file",
                      help="File with settings", metavar="FILE")
    parser.add_option("-l", "--limit", dest="limit", default=30,
                      help="Max limit", metavar="LIMIT")
    parser.add_option("-q", "--quiet", dest="verbose", default=True,
                      action="store_false", help="Don't print messages to stdout")

    (options, args) = parser.parse_args()

    logger = TicketSwapLogger() if options.verbose else None
    monitor = TicketSwapMonitor(args[0], options, logger)
    monitor.run()
