from __future__ import absolute_import, division, print_function, unicode_literals

from PySide import QtGui
from datetime import datetime, timedelta

import logging

logger = logging.getLogger(__name__)

from hydroffice.soundspeed.base.callbacks import AbstractCallbacks


class QtCallbacks(AbstractCallbacks):
    """Qt-based callbacks"""

    def __init__(self, parent):
        self.parent = parent

    def ask_date(self):
        """Ask user for date"""
        now = datetime.utcnow()
        date_msg = "Enter date as DD/MM/YYYY [default: %s]:" % now.strftime("%d/%m/%Y")
        time_msg = "Enter time as HH:MM:SS [default: %s]:" % now.strftime("%H:%M:%S")
        dt = None

        # date
        while True:
            date, ok = QtGui.QInputDialog.getText(self.parent, "Date", date_msg)
            if not ok:
                return None

            if date == "":
                dt = datetime(year=now.year, month=now.month, day=now.day)
                break

            try:
                dt = datetime.strptime(date, "%d/%m/%Y")
                break

            except ValueError:
                QtGui.QMessageBox.information(self.parent, "Invalid input",
                                              "The input date format is DD/MM/YYYY (e.g., 08/08/1980).\n"
                                              "You entered: %s" % date)
                continue

        # time
        while True:
            time, ok = QtGui.QInputDialog.getText(self.parent, "Time", time_msg)
            if not ok:
                return None

            if time == "":
                dt += timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)
                break

            try:
                in_time = datetime.strptime(time, "%H:%M:%S")
                dt += timedelta(hours=in_time.hour, minutes=in_time.minute,
                                seconds=in_time.second)
                break

            except ValueError:
                QtGui.QMessageBox.information(self.parent, "Invalid input",
                                              "The input time format is HH:MM:SS (e.g., 10:30:00).\n"
                                              "You entered: %s" % time)
                continue

        return dt

    def ask_location(self):
        """Ask user for location"""

        # latitude
        lat, ok = QtGui.QInputDialog.getDouble(self.parent, "Location", "Enter latitude as dd.ddd:",
                                               37.540, -90.0, 90.0, 7)
        if not ok:
            lat = None
        # longitude
        lon, ok = QtGui.QInputDialog.getDouble(self.parent, "Location", "Enter longitude as dd.ddd:",
                                               -42.910, -180.0, 180.0, 7)
        if not ok:
            lon = None

        if (lat is None) or (lon is None):  # return None if one of the two is invalid
            return None, None

        return lat, lon

    def ask_location_from_sis(self):
        """Ask user whether retrieving location from SIS"""
        msg = "Geographic location required for pressure/depth conversion and atlas lookup.\n" \
              "Use geographic position from SIS?\nChoose 'no' to enter position manually."
        ret = QtGui.QMessageBox.information(self.parent, "Location", msg,
                                            QtGui.QMessageBox.Ok | QtGui.QMessageBox.No)
        if ret == QtGui.QMessageBox.No:
            return False
        return True

    def ask_tss(self):
        """Ask user for transducer sound speed"""
        tss, ok = QtGui.QInputDialog.getDouble(self.parent, "TSS", "Enter transducer sound speed:",
                                               1500.0, 1000.0, 20000.0, 2)
        if not ok:
            tss = None
        return tss

    def ask_draft(self):
        """Ask user for draft"""
        draft, ok = QtGui.QInputDialog.getDouble(self.parent, "Draft", "Enter transducer draft:",
                                                 8.0, -1000.0, 1000.0, 3)
        if not ok:
            draft = None
        return draft

    def msg_tx_no_verification(self, name, protocol):
        """Profile transmitted but not verification available"""
        QtGui.QMessageBox.information(self.parent, "Profile transmitted",
                                      "Profile transmitted to \'%s\'.\n\n"
                                      "The %s protocol does not allow verification." %
                                      (name, protocol))

    def msg_tx_sis_wait(self, name):
        """Profile transmitted, SIS is waiting for confirmation"""
        QtGui.QMessageBox.information(self.parent, "Profile Transmitted",
                                      "Profile transmitted to \'%s\'.\n\n"
                                      "SIS is waiting for operator confirmation." % name)

    def msg_tx_sis_confirmed(self, name):
        """Profile transmitted, SIS confirmed"""
        QtGui.QMessageBox.information(self.parent, "Transmitted",
                                      "Reception confirmed from \'%s\'!" % name)

    def msg_tx_sis_not_confirmed(self, name, ip):
        """Profile transmitted, SIS not confirmed"""
        QtGui.QMessageBox.warning(self.parent, "Transmitted",
                                  "Profile transmitted, but \'%s\' did not confirm the recption\n\n"
                                  "Please do the following checks on SIS:\n"
                                  "1) Check sound speed file name in SIS run-time parameters "
                                  "and match date/time in SIS .asvp filename with cast date/time to ensure receipt\n"
                                  "2) Ensure SVP datagram is being distributed to this IP "
                                  "on port %d to enable future confirmations"
                                  % (name, ip))