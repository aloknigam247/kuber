class MetaInfo:
    def generate():
        pass

class MetaInfoFactory:
    __metainfo_list: dict[str, MetaInfo] = {}

    def create(metainfo: str) -> MetaInfo:
        return MetaInfoFactory.__metainfo_list[metainfo]

    def getNames() -> list[str]:
        return list(MetaInfoFactory.__metainfo_list.keys())