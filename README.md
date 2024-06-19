<pagination-template #p="paginationApi" (pageChange)="pageChangeForTable1($event)">
  <select name="pageToggle" id="pageToggle" [(ngModel)]="pagesize">
    <ng-container *ngFor="let item of createRangeForTable1(p?.getLastPage() ?? 0)">
      <option [value]="item.value">{{ item.label }}</option>
    </ng-container>
  </select>
</pagination-template>



pageChangeForTable1(newPageSize: number) {
  this.pagesize = newPageSize;
  // Perform additional operations if needed, such as fetching data with the new page size
}
