validateEndDate() {
    const fromDate = new Date(this.downTimeFromDate).getTime();
    const endDate = new Date(this.downTimeToDate).getTime();
    
    if (endDate < fromDate + 30 * 60 * 1000) {
      alert("End Date and Time cannot be less than 30 minutes after the Start Date and Time.");
      this.downTimeToDate = this.minEndDate; // Resetting to minimum valid end date and time
    }
  }
