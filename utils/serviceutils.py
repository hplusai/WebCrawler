#
# A sample service to be 'compiled' into an exe-file with py2exe.
#
# See also
#    setup.py - the distutils' setup script
#    setup.cfg - the distutils' config file for this
#    README.txt - detailed usage notes
#
# A minimal service, doing nothing else than
#    - write 'start' and 'stop' entries into the NT event log
#    - when started, waits to be stopped again.
#
import win32serviceutil
import win32service
import win32event
import win32evtlogutil

class StandartService(win32serviceutil.ServiceFramework):
    _svc_name_ = "UnknownService"
    _svc_display_name_ = "It's example class"
    _svc_deps_ = ["EventLog"]
    _svc_run_func_=None
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        import servicemanager
        # Write a 'started' event to the event log...
        win32evtlogutil.ReportEvent(self._svc_name_,
                                    servicemanager.PYS_SERVICE_STARTED,
                                    0, # category
                                    servicemanager.EVENTLOG_INFORMATION_TYPE,
                                    (self._svc_name_, ''))

        # wait for beeing stopped...
        ## Run with one parameter - Stop Event Flag hWaitStop
        win32evtlogutil.ReportEvent(self._svc_name_,
                                    servicemanager.PYS_SERVICE_STARTED,
                                    0, # category
                                    servicemanager.EVENTLOG_INFORMATION_TYPE,
                                    (str(self._svc_run_func_[0]), ''))
        self._svc_run_func_[0](self.hWaitStop)
        ## this string must put into the function _svc_run_func_ for stop looping
        ##        win32event.WaitForSingleObject(self.hWaitStop, milliseconds)

        # and write a 'stopped' event to the event log.
        win32evtlogutil.ReportEvent(self._svc_name_,
                                    servicemanager.PYS_SERVICE_STOPPED,
                                    0, # category
                                    servicemanager.EVENTLOG_INFORMATION_TYPE,
                                    (self._svc_name_, ''))


## Create Copy of Service Class and Set any parameters
## any information about RunFunc see in class UnknownService
def CreateServiceClass(ServiceName,DisplayName,RunFunc):
##    import copy
##    ret=copy.copy(UnknownService)
    StandartService._svc_name_ = ServiceName
    StandartService._svc_display_name_ = DisplayName
    StandartService._svc_run_func_=[RunFunc]
    return StandartService

if __name__ == '__main__':
    # Note that this code will not be run in the 'frozen' exe-file!!!
    win32serviceutil.HandleCommandLine(StandartService)