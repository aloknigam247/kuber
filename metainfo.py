class MetaInfo:
    pass

class MetaInfoFactory:
    __metainfo_list: dict[str, MetaInfo] = {}

    def getNames() -> list[str]:
        return list(MetaInfoFactory.__metainfo_list.keys())