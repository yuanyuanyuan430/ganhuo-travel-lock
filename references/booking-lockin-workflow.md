# Booking Lock-In Workflow

Use when the user asks to book, reserve, lock in, compare cancellable options, or turn an itinerary into actions.

## Lock-In Order

1. Lock route and dates first.
2. Verify transport to and from the destination.
3. Pick hotel area, then compare cancellable hotels.
4. Verify timed attractions, museums, parks, performances, and tours.
5. Add local transfers, restaurants, rentals, and backup indoor options.

## Lock State

Use these labels exactly:

- `已锁定`: user has chosen it, or there is booking proof/reservation proof.
- `建议锁定`: current evidence is good enough for the user to book manually.
- `待确认`: user preference or identity/detail is still missing.
- `待核验`: volatile fact needs live source check before relying on it.
- `备选`: fallback if price, weather, availability, or energy level changes.
- `不建议锁定`: risk, cost, schedule, or cancellation rule is poor.

## Checks Before Saying "Lock This"

- Dates, traveler count, child age/height rules, names and ID requirements.
- Refund, cancellation, change, deposit, and no-show rules.
- Ticket slot, entry gate, check-in time, latest arrival, and blackout dates.
- Location friction: station or airport transfer time, heat/rain exposure, stroller/luggage fit.
- Weather risk and fallback plan for beaches, mountains, islands, cruises, rafting, and outdoor shows.

## Decision Log

| Item | Status | Evidence | Change rule |
|---|---|---|---|
| City/route | 已锁定/待确认/备选 | User choice or source | Changes affect all downstream items |
| Dates | 已锁定/待确认 | User/date source | Changes require rechecking prices |
| Transport | 已锁定/待核验/备选 | Live source | Recheck before purchase |
| Hotel area/hotel | 已锁定/待核验/备选 | Live source | Recheck cancellation and room policy |
| Attractions/tickets | 已锁定/待核验/备选 | Live source | Recheck reservation and closure |
| Budget | 已锁定/待确认 | Sum of checked items | Recalculate after price changes |

## Lock Output

When the user says "锁定", output:

```markdown
## 锁定版本 v[Number]

### 已锁定
- [Decision]: [why it is locked]

### 建议锁定
- [Decision]: [source checked, why it is ready]

### 待核验
- [Fact]: [source/action needed before departure or purchase]

### 备选
- [Fallback]: [when to switch]

### 变更需确认
- [Change]: [impact]

### 用户亲自操作
- [Platform/page]: [book/pay/identity confirmation step]
```

## Booking Boundary

The agent can:

- Compare prices and policies from public or user-opened pages.
- Help fill a decision table.
- Navigate to a review page if the user explicitly asks and the platform allows it.
- Prepare the user for checkout by listing documents, passenger names, child ages, refund rules, and risk notes.

The agent must not:

- Auto-submit orders, auto-pay, or click purchase confirmation without explicit user confirmation in the current turn.
- Store or reuse passwords, SMS codes, identity numbers, payment details, cookies, or session tokens.
- Bypass captchas, waiting rooms, anti-bot checks, queue systems, rate limits, or platform terms.
- Run high-frequency price scraping, ticket sniping, resale/scalping workflows, or stealth automation.
- Claim a live price, stock, seat, room, or reservation exists without a current source.

If the user asks for prohibited automation, refuse that part and offer a compliant alternative: live comparison, reminder checklist, official-source handoff, and manual checkout steps.
