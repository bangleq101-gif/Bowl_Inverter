# Tổng hợp cuộc trao đổi thiết kế Bowl Inverter

> Tài liệu này ghi lại logic kỹ thuật đã hình thành trong cuộc trao đổi ngày 2026-08-26. Mục tiêu là để một kỹ sư/Codex/ChatGPT khác mở repo và hiểu đúng cơ cấu, không lặp lại các phương án đã bị loại.

## 1. Bài toán gốc

Thiết kế cơ cấu cơ khí chạy liên tục để nhận các tô phở/mì đã đóng nắp, tất cả đi vào ở trạng thái **ngửa**, và đầu ra phải xen kẽ:

`NGỬA / ÚP / NGỬA / ÚP / ...`

Năng suất yêu cầu: **160 tô/phút**.

Thông số sản phẩm đã cung cấp:

- Đường kính miệng: **138 mm**
- Đường kính đáy: **120 mm**
- Chiều cao: **62 mm**
- Khối lượng: **87 g**
- Dạng gần đúng: nón cụt
- Tô đã đóng nắp, đầu vào đặt đáy trên băng tải

Từ 160 tô/phút:

- Chu kỳ một tô: `60/160 = 0.375 s`
- Chỉ lật mỗi tô thứ hai -> một sự kiện lật mỗi **0.75 s**

## 2. Giai đoạn tham khảo video và lý do bỏ

Ban đầu có tham khảo các video cơ cấu alternate inverter/timing screw. Một số mô hình thử theo hướng:

- hai timing screw làm tô tự xoay;
- guide làm tô tự quay;
- wheel/paddle mô phỏng bằng animation đơn giản.

Các mô hình này bị người dùng bác bỏ vì **không đúng cơ khí thực tế** hoặc chỉ là animation nhìn có vẻ đúng nhưng không chứng minh tiếp xúc/lực/clearance.

Sau đó người dùng chốt: **không cần bám video nữa, sẽ tự mô tả nguyên lý cơ cấu**. Từ thời điểm này, mọi thiết kế phải bám mô tả của người dùng, không quay lại cơ cấu Morrison/video nếu chưa có lý do kỹ thuật mới.

## 3. Nguyên lý cơ cấu do người dùng chốt

Trình tự cơ khí:

1. Tô đi vào **timing screw**.
2. Timing screw phối hợp với **tấm nâng/guide** để nâng dần và làm tô nghiêng.
3. Tô được đưa tới góc tiền-lật, baseline hiện tại khoảng **52°**.
4. Một **cánh gạt/roller** tác động ngang lên tô được chọn để lật.
5. Tô được gạt sang phía đối diện của timing screw và đồng thời hoàn tất quá trình lật.
6. **Receiving guide** phía bên kia phải đón và kiểm soát tô; không cho free-flight mất kiểm soát.
7. Tô không được chọn lật phải đi theo nhánh return và trở lại 0°.

## 4. Ràng buộc quan trọng nhất: positive drive của timing screw

Người dùng bổ sung một yêu cầu quyết định toàn bộ kiến trúc:

> Khi tấm nâng đã làm tô **nhấc hoàn toàn khỏi mặt băng tải**, timing screw vẫn phải tiếp tục dẫn/đẩy tô theo chiều chạy và giữ phase chính xác.

Hệ quả:

- Không được dựa vào ma sát của guide để kéo tô dọc line.
- Không được mở relief của screw quá sớm.
- Trong vùng nâng phải có **positive-control overlap**:
  - lift guide chịu trọng lượng và định cao/góc;
  - screw drive flank vẫn truyền lực dọc line;
  - paddle/roller + receiving guide chỉ tiếp quản sau khi đã tạo kiểm soát chắc chắn.
- Chỉ sau khi paddle/receiving guide thực sự tiếp quản mới mở transfer relief đủ lớn để tô đi ngang qua screw.

Đây là quy tắc không được phá vỡ trong các phiên bản sau.

## 5. Baseline kinematic ban đầu

Baseline được dùng để phát triển hình học:

- Pitch: **160 mm**
- Single-start screw
- Screw: **160 rpm**
- Tốc độ dọc line: `160 mm/rev × 160 rev/min / 60 = 426.667 mm/s`
- Góc pre-flip: **52°** (tạm thời, chưa phải thông số thực nghiệm cuối)

Góc 52° được chọn bảo thủ dựa trên giả định CG chưa đo thực tế. CG của tô đóng gói vẫn là dữ liệu cần đo.

## 6. V1 – các section 0/15/30/45/52°

V1 tạo các mặt cắt timing screw tại 0°, 15°, 30°, 45°, 52° và bắt đầu định nghĩa:

- drive flank phía sau tô;
- clearance nhỏ phía drive;
- clearance lớn hơn phía leading flank;
- lift profile;
- vị trí screw phase theo X.

Kết quả quan trọng: pocket sâu nhất xấp xỉ vùng 30°, và về mặt hình học vẫn còn khoảng cách tới shaft.

Nhưng V1 chưa giải transfer và chưa phải surface CNC cuối.

## 7. V2/V2.1 – nhánh tô được lật

Thiết kế đoạn sau 52° được chia thành:

`PRE-FLIP -> FIRST CONTACT -> CONTROL OVERLAP -> RELIEF OPEN -> CROSS AXIS -> PADDLE RELEASE -> 180°`

Một baseline station đã được dùng:

- X=640: 52°, screw full drive
- X=670: paddle first contact
- X=705: ~58°, receiving guide bắt đầu nhận
- X=740: ~65°, screw full-drive cuối
- X=780: ~78°, chỉ còn trailing drive lug, relief mở mạnh hơn
- X=840: ~110°, tô vượt vùng trục
- X≈875: paddle release
- X≈920: tô ~180°

Điểm cốt lõi: **screw không buông tô ngay khi paddle chạm**.

## 8. V3 – nhánh tô không lật và dual-path screw

Tô không lật phải từ khoảng 52° quay trở lại 0° trong khi screw vẫn là master theo X.

Phát hiện quan trọng: trong cùng vùng X, screw phải đồng thời:

- giữ drive material cho tô không lật ở phía cũ;
- mở transfer window cho tô được lật đi ngang qua.

Do đó screw **không thể neck-down toàn chu vi**.

Cần section bất đối xứng:

- một sector là transfer relief/window;
- sector còn lại giữ **return-side drive lug/flank**.

## 9. V4 – swept-envelope screw đầu tiên

V4 dùng hai quỹ đạo FLIP và RETURN trong hệ tọa độ quay của screw để tạo swept-envelope 3D.

Mục tiêu:

- nhìn thấy hình dạng screw thật;
- kiểm tra material còn lại tại X≈740/780/840;
- xác nhận ý tưởng transfer window + return drive lug có thể tồn tại đồng thời.

V4 hữu ích cho topology nhưng giả định Ø120/tâm screw sau đó bị phát hiện chưa đủ tốt cho positive drive khi tô nâng cao.

## 10. V5.1 – sửa vị trí/đường kính screw để giữ positive drive

Kiểm tra contact cho thấy phôi Ø120 quá nhỏ trong vùng tô nâng cao.

Thiết kế được sửa theo hướng:

- tăng phôi lên khoảng **Ø135 mm**;
- đổi vị trí tâm screw;
- trì hoãn relief, không mở 6 mm quá sớm;
- giữ drive flank tới khi paddle/guide thực sự tiếp quản.

V5.1 đạt kiểm tra positive-drive cục bộ tại các station được thử.

## 11. V6 – lift/return guide, receiving guide và paddle-contact path

Từ quỹ đạo bowl pose đã tính, V6 sinh:

- lift/return guide;
- receiving guide;
- paddle contact path.

Nguyên tắc quan trọng: guide được sinh từ kinematics của tô, không vẽ bằng mắt.

Paddle contact path cho thấy quỹ đạo không phải một cung tròn hoàn hảo, vì vậy không nên ép ngay một paddle/wheel cứng bán kính cố định nếu chưa kiểm tra.

## 12. V7/V8/V9 – quá trình tìm cơ cấu paddle/roller

### V7

Thử fit rotor 3 cánh và radial cam. Kết quả cho thấy broad/rectangular shoe không phù hợp hoàn toàn với envelope sản phẩm.

### V8

Chuyển sang curved 3D paddle/shoe sinh từ contact path. Clearance với tô không được chọn tốt hơn, nhưng đây vẫn chưa phải giải pháp truyền lực cuối.

### V9

Thử connected rotor/hanger để kiểm tra phần kết cấu treo có đụng bowl envelope hay không. Một số clearance sơ bộ đạt nhưng vẫn là kinematic prototype.

## 13. V10 – kiểm tra nhiều tô và các lần FAIL quan trọng

V10 bắt đầu chạy nhiều tô đồng thời với:

- 160 tô/phút;
- pitch 160 mm;
- screw 160 rpm;
- 3-arm rotor 26.667 rpm.

Quan hệ phase lý tưởng:

- screw quay **360° mỗi tô**;
- rotor quay **60° mỗi tô**;
- mỗi sự kiện lật cách 2 tô -> rotor quay **120° mỗi sự kiện lật**, đúng bằng khoảng cách 3 cánh.

Nhiều vòng V10 bị FAIL và được giữ lại vì chúng cho thấy:

- gán sai arm phase có thể làm cánh khác đụng tô;
- broad rigid paddle có thể xuyên envelope sản phẩm;
- nếu các roller không làm việc vẫn nằm trong product zone, chúng có thể va tô khác;
- chỉ kiểm tra bowl #0/arm #0 là không đủ; phải kiểm tra mọi bowl và mọi arm.

## 14. Yêu cầu mới: không chấp nhận geometric penetration

Người dùng chốt rõ:

> Không được chạm/va sai; không dùng pad mềm để hợp thức hóa việc solid xuyên nhau.

Từ đó tiêu chí được tách rõ:

- **tô không được chọn / wrong roller**: bắt buộc có clearance dương đủ lớn;
- **roller đúng của tô được lật**: tiếp xúc chủ đích phải là **tangent contact ~0 gap**, không phải penetration.

## 15. V10.10 – selective high-retract roller

Giải pháp hiện tại:

- rotor 3 tay;
- chỉ roller đúng phase đi xuống vùng sản phẩm;
- các roller không active được thu lên cao khoảng **Z=170 mm**;
- thứ tự cánh theo chiều quay mô hình: **0 -> 2 -> 1**;
- active contact window khoảng **0.225 s**;
- intended contact là tangent contact.

Kết quả screening V10.10 được báo cáo:

- clearance tô không lật với roller: ~79.36 mm
- clearance tô lật với wrong roller: ~95.05 mm
- neighbor bowl clearance: ~22 mm
- bowl-to-shaft clearance được carried forward: ~5.09 mm
- intended contact: gần 0 trong sai số lưới

Đây là **PASS động học/contact-envelope sơ bộ**, chưa phải chứng minh lực/độ bền.

## 16. V11 – timing screw được sinh lại quanh tâm cuối

Không tiếp tục dịch file V5.1. Screw V11 được regenerate từ phôi quanh tâm cuối:

- phôi: **Ø135 mm**
- shaft: **Ø25 mm**
- screw axis: **Y=-21.5 mm, Z=26.5 mm**
- pitch: **160 mm**

V11 dùng swept envelope của các pose để kiểm tra lại:

- positive drive;
- shaft clearance;
- transfer-window material;
- return-side drive material.

V11 là baseline timing screw hiện tại trong repo.

## 17. V12 – web playback và lỗi đã phát hiện

V12 là viewer/web playback tự chạy, sử dụng dữ liệu pose thay vì quay tô tùy ý.

Tuy nhiên người dùng phát hiện:

> Tô chạy một lúc thì biến mất.

Nguyên nhân được xác định là logic spawn/window/loop của viewer chưa hoàn thiện. Vì vậy:

- V12 **không được xem là simulation đã pass**;
- không dùng V12 làm bằng chứng thiết kế;
- phải sửa continuous spawning/loop trước.

Ngoài ra các hình render 3D đẹp được tạo sau đó đã bị người dùng chỉ ra **sai nguyên lý**. Những hình đó chỉ là minh họa và không được dùng để suy ngược cơ cấu.

## 18. Trạng thái kỹ thuật hiện tại

Baseline đáng tin cậy nhất hiện tại:

- product geometry và throughput đã khóa;
- timing/phase 160 rpm screw + 26.667 rpm rotor nhất quán;
- positive-drive principle đã khóa;
- dual-path/asymmetric transfer screw principle đã khóa;
- V10.10 selective high-retract roller là concept actuation hiện tại;
- V11 là timing screw baseline hiện tại;
- V12 viewer còn bug và cần sửa.

## 19. Những gì CHƯA được chứng minh

Chưa được coi là thiết kế chế tạo cuối vì còn thiếu:

- CG thực của từng cấu hình sản phẩm;
- hệ số ma sát bowl/guide/roller;
- độ cứng và biến dạng thành tô/nắp;
- lực tiếp xúc cần thiết để vượt tipping point;
- lực động do 160 tô/phút;
- torque/deflection của shaft;
- bearing loads;
- fatigue rotor/arm;
- dung sai lắp ráp và khả năng chỉnh;
- vật liệu food-grade và sanitation;
- kiểm tra tolerance stack;
- test thực tế với sản phẩm.

## 20. Quy tắc tiếp tục dự án

1. Không thay đổi nguyên lý đã khóa nếu không ghi rõ lý do và kết quả kiểm tra.
2. Mọi animation phải lấy pose từ kinematics/contact model, không quay bằng tay cho đẹp.
3. Mọi phương án mới phải kiểm tra nhiều tô đồng thời.
4. Wrong arm/roller tuyệt đối không chạm tô.
5. Intended contact phải là tiếp xúc chủ đích/tangent, không geometric penetration.
6. Screw phải tiếp tục positive drive sau khi bowl rời belt.
7. Không free-flight trong transfer.
8. Không dùng ảnh render AI làm geometry kỹ thuật.
9. Khi một phương án FAIL, giữ lại lý do FAIL để không lặp lại.
10. Trước CNC cần chuyển từ kinematic model sang force/contact/structural validation.