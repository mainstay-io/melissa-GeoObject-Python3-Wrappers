import enum
from typing import TypeAlias, Literal

import deprecated


InputParameterKey: TypeAlias = Literal[
    'MAK',
    'AddressKey',
    'Zip',
    'Plus4',
    'Latitude',
    'Longitude',
]

# noinspection SpellCheckingInspection
OutputParameterKey: TypeAlias = Literal[
    'BlockSuffix',
    'CBSAcode',
    'CBSATitle',
    'CBSALevel',
    'CBSADivisionCode',
    'CBSADivisionTitle',
    'CBSADivisionLevel',
    'CensusBlock',
    'CensusKey',
    'CensusKeyDecennial',
    'CensusTract',
    'CountyFips',
    'CountyName',
    'CountySubdivisionCode',
    'CountySubdivisionName',
    'ElementarySchoolDistrictCode',
    'ElementarySchoolDistrictName',
    'Latitude',
    'Longitude',
    'LSAD',
    'PlaceCode',
    'PlaceName',
    'Results',
    'SecondarySchoolDistrictCode',
    'SecondarySchoolDistrictName',
    'StateDistrictLower',
    'StateDistrictUpper',
    'TimeZone',
    'TimeZoneCode',
    'UnifiedSchoolDistrictCode',
    'UnifiedSchoolDistrictName',
]


# mdGeo IntEnumerations
class ProgramStatus(enum.IntEnum):
    ErrorNone = 0
    ErrorOther = 1
    ErrorOutOfMemory = 2
    ErrorRequiredFileNotFound = 3
    ErrorFoundOldFile = 4
    ErrorDatabaseExpired = 5
    ErrorLicenseExpired = 6


class AccessType(enum.IntEnum):
    Local = 0
    Remote = 1


class DiacriticsMode(enum.IntEnum):
    Auto = 0
    On = 1
    Off = 2


class StandardizeMode(enum.IntEnum):
    ShortFormat = 0
    LongFormat = 1
    AutoFormat = 2


class SuiteParseMode(enum.IntEnum):
    ParseSuite = 0
    CombineSuite = 1


class AliasPreserveMode(enum.IntEnum):
    ConvertAlias = 0
    PreserveAlias = 1


class AutoCompletionMode(enum.IntEnum):
    AutoCompleteSingleSuite = 0
    AutoCompleteRangedSuite = 1
    AutoCompletePlaceHolderSuite = 2
    AutoCompleteNoSuite = 3


class ResultCdDescOpt(enum.IntEnum):
    ResultCodeDescriptionLong = 0
    ResultCodeDescriptionShort = 1


class MailboxLookupMode(enum.IntEnum):
    MailboxNone = 0
    MailboxExpress = 1
    MailboxPremium = 2


# noinspection PyPep8Naming
class mdGeo:
    """
    Melissa has documentation spread uniquely across multiple subdomains:
    * https://docs.melissa.com/on-premise-api/geocoder-object/geocoder-object-reference-guide.html
    * https://wiki.melissadata.com/index.php?title=GeoCoder_Object
    * https://www.melissa.com/reference-guides/geocoder-object
    """

    def SetPathToGeoCodeDataFiles(self, p1: str) -> None: ...
    def SetPathToGeoPointDataFiles(self, p1: str) -> None: ...
    def SetPathToGeoCanadaDataFiles(self, p1: str) -> None: ...
    def SetLicenseString(self, License: str) -> None: ...
    def InitializeDataFiles(self) -> ProgramStatus: ...
    def GetInitializeErrorString(self) -> str: ...

    def GetBuildNumber(self) -> str: ...
    def GetDatabaseDate(self) -> str: ...
    def GetExpirationDate(self) -> str: ...
    def GetLicenseExpirationDate(self) -> str: ...
    def GetLastUsageLogMessage(self) -> str: ...

    def WriteToLogFile(self, logFile: str) -> bool: ...

    # These functions have bugs in Melissa's implementation.
    def ComputeDistance(self, Latitude1: str, Longitude1: str, Latitude2: str, Longitude2: str) -> str: ...
    def ComputeBearing(self, Latitude1: str, Longitude1: str, Latitude2: str, Longitude2: str) -> str: ...

    def SetInputParameter(self, key: InputParameterKey, val: str) -> str: ...
    def FindGeo(self) -> None: ...
    def GetOutputParameter(self, key: OutputParameterKey) -> str: ...
    def GetResults(self) -> str: ...
    def GetResultCodeDescription(
        self, resultCode: str, opt: ResultCdDescOpt = ResultCdDescOpt.ResultCodeDescriptionLong
    ) -> str: ...

    # These methods aren't deprecated in the documentation, but they should be.
    def GetCensusKey(self) -> str: ...
    def GetCountySubdivisionCode(self) -> str: ...
    def GetCountySubdivisionName(self) -> str: ...
    def GetElementarySchoolDistrictCode(self) -> str: ...
    def GetElementarySchoolDistrictName(self) -> str: ...
    def GetSecondarySchoolDistrictCode(self) -> str: ...
    def GetSecondarySchoolDistrictName(self) -> str: ...
    def GetStateDistrictLower(self) -> str: ...
    def GetStateDistrictUpper(self) -> str: ...
    def GetUnifiedSchoolDistrictCode(self) -> str: ...
    def GetUnifiedSchoolDistrictName(self) -> str: ...
    def GetBlockSuffix(self) -> str: ...

    @deprecated.deprecated(reason='Use FindGeo instead.')
    def GeoCode(self, Zip: str, Plus4: str) -> ProgramStatus: ...
    @deprecated.deprecated(reason='Use FindGeo instead.')
    def GeoPoint(self, Zip: str, Plus4: str, DeliveryPointCode: str) -> ProgramStatus: ...  # deprecated
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCBSACode(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCBSADivisionCode(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCBSADivisionLevel(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCBSADivisionTitle(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCBSALevel(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCBSATitle(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCensusBlock(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCensusTract(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCountyFips(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetCountyName(self) -> str: ...
    @deprecated.deprecated(reason='Use GetResults instead.')
    def GetErrorCode(self) -> str: ...  # deprecated
    @deprecated.deprecated(reason='Use GetResults instead.')
    def GetLatitude(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetLongitude(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetPlaceCode(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetPlaceName(self) -> str: ...
    @deprecated.deprecated(reason='Use GetResults instead.')
    def GetStatusCode(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetTimeZone(self) -> str: ...
    @deprecated.deprecated(reason='Use GetOutputParameter instead.')
    def GetTimeZoneCode(self) -> str: ...
    @deprecated.deprecated(reason='Use InitializeDataFiles instead.')
    def Initialize(self, DataPath: str, IndexPath: str) -> ProgramStatus: ...
    @deprecated.deprecated(reason='Use SetInputParameter instead.')
    def SetLatitude(self, latitude: str) -> None: ...
    @deprecated.deprecated(reason='Use SetInputParameter instead.')
    def SetLongitude(self, longitude: str) -> None: ...
