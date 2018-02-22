
def MinerTransaction():
    return b'\x00'


def IssueTransaction():
    return b'\x01'


def ClaimTransaction():
    return b'\x02'


def EnrollmentTransaction():
    return b'\x20'


def VotingTransaction():
    return b'\x24'


def RegisterTransaction():
    return b'\x40'


def ContractTransaction():
    return b'\x80'


def StateTransaction():
    return b'\x90'


def AgencyTransaction():
    return b'\xb0'


def PublishTransaction():
    return b'\xd0'


def InvocationTransaction():
    return b'\xd1'
