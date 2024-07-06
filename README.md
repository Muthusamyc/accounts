select cattyp.CategoryTypeID,cattyp.CategoryID,catid.CategoryName,cattyp.CategoryType,cattyp.IsActive,cattyp.CreatedBy,cattyp.CreatedDate,catid.ModifiedBy,cattyp.ModifiedDate
			from IT.CategoryTyp as cattyp
			left join IT.Category catid on catid.ITCategoryID=cattyp.CategoryID
