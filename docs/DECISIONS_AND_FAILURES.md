# Decisions, Rejected Concepts and Failed Iterations

Mục tiêu của file này là ngăn việc lặp lại những hướng đã được thử và bác bỏ.

## A. Các nguyên lý đã bị loại

### 1. Hai timing screw/guide làm tô tự xoay

Bị loại vì không phản ánh đúng cơ cấu mà người dùng muốn chế tạo và khó chứng minh positive control thực.

### 2. Animation quay tô thủ công

Bị loại hoàn toàn.

Một viewer chỉ có giá trị khi pose của tô được lấy từ trajectory/kinematic/contact model. Không được quay tô theo keyframe chỉ để hình ảnh trông đúng.

### 3. Dựa vào băng tải sau khi tô đã được nâng khỏi belt

Bị loại theo yêu cầu trực tiếp của người dùng.

Khi bowl không còn tiếp xúc belt, timing screw vẫn phải truyền lực dọc line và giữ phase.

### 4. Mở transfer relief sớm

Bị loại vì làm mất drive flank trước khi paddle/receiving guide tiếp quản.

### 5. Neck-down cả chu vi screw tại transfer

Bị loại vì tô không lật vẫn cần return-side drive lug ở cùng vùng X.

Transfer relief phải bất đối xứng theo chu vi.

### 6. Free-flight để hoàn tất lật

Bị loại. Receiving guide phải kiểm soát bowl qua vùng sau tipping point.

### 7. Broad rigid paddle

Các thử nghiệm V7/V10 cho thấy bản/cánh rộng dễ xuyên envelope hoặc chạm sai tô. Không được quay lại broad paddle nếu chưa có collision model mới chứng minh được.

### 8. Dùng pad mềm để hợp thức hóa penetration

Bị người dùng bác bỏ.

Không được nói rằng solid xuyên 2–3 mm là chấp nhận được chỉ vì có pad mềm. Geometry CAD phải không penetration. Intended contact phải là tangent/contact đúng nghĩa.

### 9. Để các roller không active nằm trong product zone

Bị loại trong V10. Các wrong rollers có thể đụng tô khác.

Giải pháp hiện tại: inactive rollers retract upward, baseline khoảng Z=170 mm.

### 10. Gán sai thứ tự arm

Một số V10 FAIL do mapping arm phase sai.

Thứ tự cho chiều quay baseline hiện tại: **0 -> 2 -> 1**.

## B. Các phiên bản và lý do thay đổi

### V1

- Mục tiêu: section 0/15/30/45/52°.
- Hữu ích: hình thành drive flank và lift profile.
- Hạn chế: chưa giải dual-path transfer.

### V2/V2.1

- Mục tiêu: selected-bowl transfer 52° -> 180°.
- Hữu ích: định nghĩa overlap/relief/crossover.
- Hạn chế: chưa ghép return branch.

### V3

- Mục tiêu: return branch 52° -> 0°.
- Phát hiện quyết định: screw phải giữ drive lug cho return branch trong khi mở crossover sector.

### V4

- Mục tiêu: swept-envelope 3D đầu tiên.
- Hữu ích: chứng minh topology dual-path có thể tồn tại.
- FAIL/obsolete point: phôi Ø120/tâm screw không đủ tốt khi bowl nâng cao.

### V5.1

- Sửa OD/axis/relief timing.
- Positive-drive cục bộ cải thiện.
- Sau đó được thay bởi V11 regenerate quanh axis cuối.

### V6

- Sinh lift/return guide, receiving guide, paddle-contact path.
- Contact path cho thấy không nên ép paddle thành một cung tròn đơn giản.

### V7

- First rotor/paddle fitting.
- Broad/simple shoe không đạt hình học mong muốn.

### V8

- Curved shoe study.
- Clearance với tô không chọn tốt hơn.
- Chưa phải force-applying final solution.

### V9

- Connected rotor/hanger prototype.
- Chỉ là kiểm tra đường treo và clearance sơ bộ.

### V10.0

- Multi-bowl check đầu tiên.
- FAIL do một phần classification/intended-contact logic và axis assumptions chưa đúng.

### V10.1

- Sửa screw-axis và mapping intended arms.
- Vẫn FAIL ở wrong-arm/shaft thresholds.

### V10.2–V10.4

- Thử dịch axis/đổi paddle geometry/clearance.
- Một số phương án tránh được một lỗi nhưng tạo lỗi khác.
- Không được coi là baseline.

### V10.6

- Thử strict no-penetration curved paddle.
- Không thể chỉ offset curve đơn giản mà vẫn giữ chức năng force-contact mong muốn.

### V10.7

- Linear cam roller + normal follower.
- Intended tangent contact rất tốt.
- FAIL: wrong roller vẫn có thể xâm nhập bowl envelope.

### V10.8/V10.9

- Selective cam và sửa arm phase.
- Vẫn FAIL vì inactive/wrong roller trajectory chưa thật sự ra khỏi product zone.

### V10.10

- High-retract selective roller.
- Inactive rollers park above product envelope.
- Current preliminary PASS.

### V11

- Screw được regenerate quanh axis cuối thay vì dịch solid cũ.
- Current screw baseline.

### V12

- Web playback prototype.
- Known bug: bowls disappear after a short time because spawn/loop/window logic is incomplete.
- Không được coi là simulation pass.

## C. Hình ảnh AI/render

Trong cuộc trao đổi có tạo một số hình render 3D đẹp. Người dùng đã chỉ ra chúng **sai nguyên lý**.

Quy tắc:

- Ảnh AI chỉ được dùng làm presentation/reference.
- Không được lấy hình render làm căn cứ CAD.
- Không được chỉnh cơ cấu thật để giống ảnh render.
- Source of truth là trajectory, CAD và validation data.

## D. Tiêu chí FAIL bắt buộc

Một phương án phải đánh dấu FAIL nếu có bất kỳ điều nào sau:

- wrong roller chạm bowl;
- unselected bowl chạm paddle/roller;
- intended rigid bodies xuyên nhau;
- screw shaft cắt vào product envelope;
- bowl mất positive drive trước takeover;
- guide phải dựa vào friction để kéo bowl theo X;
- free-flight không kiểm soát;
- neighbor bowls va nhau;
- timing phase không tạo đúng sự kiện lật mỗi 0.75 s;
- simulation dùng animation giả thay vì pose tính toán.

## E. Không tự ý thay đổi baseline

Nếu muốn thay đổi một trong các mục sau, phải tạo version mới và ghi lý do:

- 160 bowls/min
- pitch 160 mm
- screw 160 rpm
- 3-arm rotor 26.667 rpm
- positive-drive requirement
- dual-path/asymmetric transfer screw
- no-free-flight requirement
- zero geometric penetration rule
- inactive roller retraction concept
- corrected screw axis Y=-21.5, Z=26.5

Các thông số có thể được tối ưu sau, nhưng không được thay âm thầm.