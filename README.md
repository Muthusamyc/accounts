pageChangeForTable1(value: any) {
  if (value !== null && value !== undefined) {
    this.pagesize = Number(value); // Convert to number if necessary
    // Other logic related to page change
  }
}
