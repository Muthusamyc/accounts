TS2769: No overload matches this call.
  Overload 1 of 3, '(locales?: LocalesArgument, options?: DateTimeFormatOptions | undefined): string', gave the following error.
    Argument of type '{ timeZone: string; hour12: boolean; year: string; month: string; day: string; hour: string; minute: string; second: string; }' is not assignable to parameter of type 'DateTimeFormatOptions'.
      Types of property 'year' are incompatible.
        Type 'string' is not assignable to type '"numeric" | "2-digit" | undefined'.
  Overload 2 of 3, '(locales?: string | string[] | undefined, options?: DateTimeFormatOptions | undefined): string', gave the following error.
    Argument of type '{ timeZone: string; hour12: boolean; year: string; month: string; day: string; hour: string; minute: string; second: string; }' is not assignable to parameter of type 'DateTimeFormatOptions'.
