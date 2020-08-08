create_cftc_cit_supplement_table_cmd = """
    CREATE TABLE cftc_cit_supplement (
    date DATE NOT NULL,
    Market_and_Exchange_Names TEXT NOT NULL,
    CFTC_Contract_Market_Code BIGINT NOT NULL,
    CFTC_Market_Code TEXT NOT NULL,
    CFTC_Region_Code BIGINT NOT NULL,
    CFTC_Commodity_Code BIGINT NOT NULL,
    Open_Interest_All BIGINT NOT NULL,
    NComm_Positions_Long_All_NoCIT BIGINT NOT NULL,
    NComm_Positions_Short_All_NoCIT BIGINT NOT NULL,
    NComm_Postions_Spread_All_NoCIT BIGINT NOT NULL,
    Comm_Positions_Long_All_NoCIT BIGINT NOT NULL,
    Comm_Positions_Short_All_NoCIT BIGINT NOT NULL,
    Tot_Rept_Positions_Long_All BIGINT NOT NULL,
    Tot_Rept_Positions_Short_All BIGINT NOT NULL,
    NonRept_Positions_Long_All BIGINT NOT NULL,
    NonRept_Positions_Short_All BIGINT NOT NULL,
    CIT_Positions_Long_All BIGINT NOT NULL,
    CIT_Positions_Short_All BIGINT NOT NULL,
    Change_Open_Interest_All BIGINT,
    Change_NonComm_Long_All_NoCIT BIGINT,
    Change_NonComm_Short_All_NoCIT BIGINT,
    Change_NonComm_Spread_All_NoCIT BIGINT,
    Change_Comm_Long_All_NoCIT BIGINT,
    Change_Comm_Short_All_NoCIT BIGINT,
    Change_Tot_Rept_Long_All BIGINT,
    Change_Tot_Rept_Short_All BIGINT,
    Change_NonRept_Long_All BIGINT,
    Change_NonRept_Short_All BIGINT,
    Change_CIT_Long_All BIGINT,
    Change_CIT_Short_All BIGINT,
    Pct_Open_Interest_All FLOAT NOT NULL,
    Pct_OI_NonComm_Long_All_NoCIT FLOAT NOT NULL,
    Pct_OI_NonComm_Short_All_NoCIT FLOAT NOT NULL,
    Pct_OI_NonComm_Spread_All_NoCIT FLOAT NOT NULL,
    Pct_OI_Comm_Long_All_NoCIT FLOAT NOT NULL,
    Pct_OI_Comm_Short_All_NoCIT FLOAT NOT NULL,
    Pct_OI_Tot_Rept_Long_All_NoCIT FLOAT NOT NULL,
    Pct_OI_Tot_Rept_Short_All_NoCIT FLOAT NOT NULL,
    Pct_OI_NonRept_Long_All_NoCIT FLOAT NOT NULL,
    Pct_OI_NonRept_Short_All_NoCIT FLOAT NOT NULL,
    Pct_OI_CIT_Long_All FLOAT NOT NULL,
    Pct_OI_CIT_Short_All FLOAT NOT NULL,
    Traders_Tot_All BIGINT NOT NULL,
    Traders_NonComm_Long_All_NoCIT BIGINT NOT NULL,
    Traders_NonComm_Short_All_NoCIT BIGINT NOT NULL,
    Traders_NonComm_Spread_All_NoCIT BIGINT NOT NULL,
    Traders_Comm_Long_All_NoCIT BIGINT NOT NULL,
    Traders_Comm_Short_All_NoCIT BIGINT NOT NULL,
    Traders_Tot_Rept_Long_All_NoCIT BIGINT NOT NULL,
    Traders_Tot_Rept_Short_All_NoCIT BIGINT NOT NULL,
    Traders_CIT_Long_All BIGINT NOT NULL,
    Traders_CIT_Short_All BIGINT NOT NULL,
    Contract_Units TEXT NOT NULL,
    PRIMARY KEY (date, Market_and_Exchange_Names));"""